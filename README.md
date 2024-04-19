# DevOps Exercise: Deploying a Secure Application on Kubernetes

## Context and Objective

You have been hired as a DevOps Engineer at a streaming services company. Your task is to deploy new microservices for user registration and counting on the platform. The microservices include:

1. FastAPI service
2. PostgreSQL database
3. PGAdmin administration interface

### Roadmap

To successfully complete the assignment, follow these steps:

1. Define appropriate Kubernetes objects for optimal deployment.
2. Write Dockerfile for FastAPI microservice.
3. Create a subdomain and DNS registration.
4. Use Rancher's default storage class for managing storage.
5. Deploy 3 replicas of the application.
6. Implement HorizontalPodAutoscaler for scalability.
7. Prepare a backup plan for the cluster using K3s client.
8. Secure the API with SSL certificates.

## Deliverables

In the provided zip file, include the following:

### Configuration Files

- **YAML-STANDARD**: All configurations using Kubernetes YAML files.
- **HELM**: All configurations for Helm deployment.
- **KUSTOMIZE**: All configurations for Kustomize deployment.

### Logs

- Log files for FastAPI, PostgreSQL, and PGAdmin microservices.

### Backup

- Backup file of the ETCD database after deploying configurations.

## Tips

- Expose each microservice via a service.
- Use ingress to connect to the FastAPI application.
- Choose appropriate objects based on the application type and confidentiality.
- Populate the database using the `/docs` route of FastAPI.
- Access user list via `/users` and count all users via `/users/count` routes.

## Running Services (Images)








