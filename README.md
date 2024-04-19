# Secure Application Deployment Project 

## Introduction
My task here was to deploy three microservices to facilitate user registration and counting on the platform. This report outlines the deployment process, including the choice of Kubernetes objects, Dockerfile creation for the FastAPI microservice, setup of Rancher's default storage class, implementation of HorizontalPodAutoscaler (HPA), SSL certificate integration, and backup plan using the K3s client.

## Deployment Approach
I followed the provided roadmap and deployed the microservices using three different methods: Kubernetes standard YAML files, Helm charts, and Kustomize configurations.
 The application is available on the following repository:  [kubernetes-devops-project.git](https://github.com/DataScientest/kubernetes-devops-project)


### 1. Kubernetes Standard Deployment
In the YAML-STANDARD directory, I created Kubernetes YAML files for each microservice, ensuring appropriate configuration for services, deployments, and persistent volume claims (PVCs). The deployments included three replicas for scalability and a HorizontalPodAutoscaler based on CPU consumption.

### 2. Helm Deployment
Using the HELM directory, I developed Helm charts for each microservice, specifying configurations such as service types, image versions, and resource requests. Helm provided a convenient way to manage complex deployments with customizable values for different environments.

### 3. Kustomize Deployment
In the KUSTOMIZE directory, I utilized Kustomize to generate customized Kubernetes manifests for each microservice. Kustomize allowed me to overlay configurations for different environments and manage variations without duplicating YAML files.

## Deliverables
To validate the exercise, I prepared the following deliverables in a zip format:

1. **YAML-STANDARD Directory**: Contains Kubernetes YAML files for standard deployment.
2. **HELM Directory**: Includes Helm charts for deployment using Helm.
3. **KUSTOMIZE Directory**: Consists of Kustomize configurations for deployment using Kustomize.
4. **Microservices Logs**: Log files for FastAPI, PostgreSQL, and PGAdmin microservices.
5. **ETCD Database Backup**: Backup file of the ETCD database after deployment.
6. **Documentation**: Detailed documentation explaining the deployment process and configurations.

## Conclusion
This project demonstrates the successful deployment of secure microservices using Kubernetes, Helm, and Kustomize. By leveraging these tools and following best practices, we have established a robust infrastructure for managing user registration and counting on the streaming platform.


