# e-commerce-app

![image](https://github.com/shubhama-d/e-commerce-app/assets/131587208/c580208b-9215-4043-b9bd-1a0a4b2180a7)
![image](https://github.com/shubhama-d/e-commerce-app/assets/131587208/8e0ffbf4-19c3-4118-97e6-e057db917b82)

And here's an example of the Azure DevOps YAML pipeline configuration:

# azure-pipeline.yml

trigger:
  branches:
    exclude:
      - '*'

pool:
  vmImage: 'ubuntu-latest'

variables:
  - group: 'docker-credentials' # Azure DevOps variable group containing Docker Hub credentials

stages:
  - stage: BuildAndPush
    displayName: 'Build and Push Docker Images'
    jobs:
      - job: BuildAndPushJob
        displayName: 'Build and Push'
        steps:
          - script: |
              docker build -t myimage:latest .
              docker login -u $(DOCKER_USERNAME) -p $(DOCKER_PASSWORD)
              docker tag myimage:latest $(DOCKER_USERNAME)/myimage:latest
              docker push $(DOCKER_USERNAME)/myimage:latest

  - stage: ProvisionAKSCluster
    displayName: 'Provision AKS Cluster'
    jobs:
      - job: ProvisionAKSClusterJob
        displayName: 'Provision AKS Cluster'
        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: '3.x'
              addToPath: true

          - task: AzureCLI@2
            inputs:
              azureSubscription: 'my-azure-subscription'
              scriptType: 'bash'
              scriptLocation: 'inlineScript'
              inlineScript: |
                cd terraform
                terraform init
                terraform plan -out=tfplan -input=false
                terraform apply -input=false -auto-approve tfplan

          - task: TerraformInstaller@0
            inputs:
              terraformVersion: 'latest'

          - task: TerraformTaskV1@0
            inputs:
              provider: 'azurerm'
              command: 'init'
              workingDirectory: 'terraform'

          - task: TerraformTaskV1@0
            inputs:
              provider: 'azurerm'
              command: 'plan'
              commandOptions: '-out=tfplan -input=false'
              workingDirectory: 'terraform'

          - task: TerraformTaskV1@0
            inputs:
              provider: 'azurerm'
              command: 'apply'
              commandOptions: '-input=false -auto-approve tfplan'
              workingDirectory: 'terraform'

  - stage: DeployToAKS
    displayName: 'Deploy to AKS Cluster'
    jobs:
      - job: DeployToAKSJob
        displayName: 'Deploy to AKS Cluster'
        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: '3.x'
              addToPath: true

          - task: AzureCLI@2
            inputs:
              azureSubscription: 'my-azure-subscription'
              scriptType: 'bash'
              scriptLocation: 'inlineScript'
              inlineScript: |
                # Set up Kubernetes credentials
                az aks get-credentials --resource-group my-aks-resource-group --name my-aks-cluster

                # Deploy Kubernetes manifests
                kubectl apply -f kubernetes

