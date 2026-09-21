# 🗳️ Project 3 — Cloud-Native Voting App Automation

A DevOps and cloud-native project focused on automating the deployment and management of a distributed voting application.

## 📌 Project Overview

The project uses an existing distributed voting application and builds a complete DevOps and cloud-native deployment workflow around it.

The application consists of five main services:

- 🗳️ Python Vote Application
- 📊 Node.js Result Application
- ⚙️ .NET Worker
- 🔴 Redis
- 🐘 PostgreSQL

The project starts with local Docker-based execution and progressively introduces cloud infrastructure, configuration management, Kubernetes orchestration, networking, persistent storage, security, monitoring, and automation.

### Application Flow

```text
User
 │
 ├──────────────► Vote App
 │                    │
 │                    ▼
 │                  Redis
 │                    │
 │                    ▼
 │                  Worker
 │                    │
 │                    ▼
 │               PostgreSQL
 │                    ▲
 │                    │
 └──────────────► Result App

```

## 🛠️ Technologies Used

### Application

- Python
- Node.js
- .NET
- Redis
- PostgreSQL

### Containerization

- Docker
- Docker Compose

### Cloud & Infrastructure

- AWS
- Amazon EC2
- Amazon VPC
- AWS Security Groups
- Terraform

### Configuration Management

- Ansible
- Linux
- Bash

### Container Orchestration

- Kubernetes
- Minikube
- Kubernetes Deployments
- Kubernetes Services
- Kubernetes Ingress
- Kubernetes ConfigMaps
- Kubernetes Secrets
- Persistent Volumes
- Persistent Volume Claims

### Monitoring & Observability

- Prometheus
- Grafana

### Automation

- Python
- Kubernetes API automation

### Version Control

- Git
- GitHub

## 📂 Project Structure

```text
project-3-voting-devops/
│
├── application/
│   ├── vote/
│   ├── result/
│   ├── worker/
│   ├── healthchecks/
│   ├── seed-data/
│   └── docker-compose.yml
│
├── terraform/
│   ├── provider.tf
│   ├── variables.tf
│   ├── vpc.tf
│   ├── security_group.tf
│   ├── ec2.tf
│   └── outputs.tf
│
├── ansible/
│   ├── inventory.ini
│   └── playbook.yml
│
├── kubernetes/
│   ├── namespace/
│   ├── postgres/
│   ├── redis/
│   ├── vote/
│   ├── worker/
│   ├── result/
│   ├── ingress/
│   └── secrets/
│
├── python/
│   └── k8s_health_check.py
│
├── monitoring/
│   ├── prometheus/
│   └── grafana/
│
├── scripts/
│
├── .gitignore
└── README.md

```
## 🏗️ Infrastructure Architecture

Terraform is used to provision the AWS infrastructure required for the project.

The infrastructure follows this structure:

```text
                        AWS
                         │
                         ▼
                    ┌─────────┐
                    │   VPC   │
                    │10.0.0.0/16
                    └────┬────┘
                         │
                         ▼
                 ┌──────────────┐
                 │ Public Subnet│
                 │ 10.0.1.0/24 │
                 └──────┬───────┘
                        │
          ┌─────────────┴─────────────┐
          │                           │
          ▼                           ▼
 ┌─────────────────┐         ┌─────────────────┐
 │ Internet Gateway│         │ Security Group  │
 └────────┬────────┘         └────────┬────────┘
          │                           │
          └─────────────┬─────────────┘
                        │
                        ▼
                ┌───────────────┐
                │   EC2 Server  │
                │    Ubuntu     │
                └───────────────┘
```

### Terraform Resources

Terraform provisions:

- VPC
- Public Subnet
- Internet Gateway
- Public Route Table
- Route Table Association
- Security Group
- EC2 Instance

### Infrastructure Flow

```text
Terraform
    │
    ▼
AWS Infrastructure
    │
    ├── VPC
    ├── Subnet
    ├── Internet Gateway
    ├── Route Table
    ├── Security Group
    └── EC2
```

The infrastructure configuration is maintained as code so that the AWS environment can be recreated consistently from the Terraform configuration.

## 🐳 Docker & Application Deployment

Docker is used to containerize the voting application and run its distributed services consistently across development and deployment environments.

### Application Containers

The application consists of the following containers:

```text
Vote Application
      │
      ├── Python
      │
      ▼
     Redis
      │
      ▼
    Worker
      │
      ▼
 PostgreSQL
      ▲
      │
 Result Application
```

### Docker Compose

Docker Compose is used to run the complete application locally with multiple interconnected services.

The Compose environment contains:

- Vote application
- Result application
- Worker
- Redis
- PostgreSQL

### Docker Tasks Completed

- Built Docker images for the application services
- Configured Docker Compose
- Configured service-to-service communication
- Added application health checks
- Fixed health-check script permissions
- Started all application containers
- Verified container health and status
- Tested the complete voting workflow

### Local Application Ports

```text
Vote Application    → http://localhost:8080
Result Application  → http://localhost:8081
```

The complete voting flow was tested successfully using Docker Compose before moving the application to Kubernetes.

## 🐧 Linux Server & Ansible

Ubuntu Linux was used as the server environment for deploying and managing the application.

Ansible was used to automate server configuration and application deployment tasks.

### Linux Server Setup

- Created an Ubuntu EC2 server
- Configured SSH access
- Configured AWS Security Group rules
- Installed Docker
- Installed Docker Compose
- Enabled and started the Docker service
- Added the Ubuntu user to the Docker group

### Ansible Automation

The Ansible playbook automates the server configuration process.

The playbook performs tasks such as:

- Updating the package repository
- Installing Docker and Docker Compose
- Starting and enabling the Docker service
- Configuring Docker access for the Ubuntu user
- Cloning the Project 3 repository
- Setting executable permissions for health-check scripts
- Starting the voting application using Docker Compose

### Automation Flow

```text
Ansible
   │
   ▼
Ubuntu EC2 Server
   │
   ├── Install Docker
   ├── Configure Docker
   ├── Clone Project
   ├── Configure Health Checks
   └── Start Application
```

The Ansible configuration is maintained as code so the server setup can be reproduced instead of performing every configuration step manually.

## ☸️ Kubernetes Deployment

Kubernetes was used to deploy and manage the voting application's distributed services.

The Kubernetes deployment was created independently rather than directly using the original Kubernetes manifests from the application repository.

### Kubernetes Components

The application was deployed using the following workloads:

- PostgreSQL
- Redis
- Vote application
- Worker
- Result application

Each component runs as a Kubernetes workload and communicates through Kubernetes Services.

### Kubernetes Architecture

```text
                    Kubernetes Cluster
                           │
                    project3 Namespace
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
    Vote App            Result App          Worker
        │                  │                  │
        ▼                  │                  ▼
      Redis ◄──────────────┘              PostgreSQL
        │                                      ▲
        └──────────────────────────────────────┘
```

### Kubernetes Resources

The project uses:

- Namespace
- Deployments
- Services
- ConfigMaps
- Secrets
- PersistentVolumeClaims
- Ingress

### Kubernetes Deployment Tasks

- Created a dedicated `project3` namespace
- Created PostgreSQL deployment
- Created Redis deployment
- Created Vote application deployment
- Created Worker deployment
- Created Result application deployment
- Created Kubernetes Services
- Configured service-to-service communication
- Configured application health checks
- Configured PostgreSQL persistent storage
- Configured Kubernetes Secrets
- Configured Ingress routing
- Verified all application pods
- Tested the complete voting workflow

### Final Pod Status

```text
PostgreSQL → Running
Redis      → Running
Vote       → Running
Worker     → Running
Result     → Running
```

The complete voting flow was verified inside Kubernetes:

```text
Vote Application
       │
       ▼
     Redis
       │
       ▼
     Worker
       │
       ▼
  PostgreSQL
       │
       ▼
 Result Application
```

## 🌐 Kubernetes Ingress

Kubernetes Ingress was configured to provide HTTP routing to the application services.

Instead of exposing every application service directly, Ingress provides a single entry point for HTTP traffic and routes requests to the appropriate Kubernetes Service.

### Ingress Architecture

```text
                         User
                           │
                           ▼
                     ┌──────────┐
                     │ Ingress  │
                     └────┬─────┘
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
        Vote Service            Result Service
              │                       │
              ▼                       ▼
          Vote Pod                Result Pod
```

### Ingress Routing

The Ingress configuration routes incoming HTTP requests to:

- Vote Service
- Result Service

### Ingress Tasks Completed

- Created Kubernetes Ingress configuration
- Configured HTTP routing
- Connected Ingress to Kubernetes Services
- Verified routing to the application services
- Tested application access through the configured routes

Ingress provides a cleaner networking layer for accessing the application services within the Kubernetes environment.

## 💾 Persistent Storage

Persistent storage was configured for PostgreSQL so that database data is stored separately from the lifecycle of the PostgreSQL pod.

### Storage Architecture

```text
                PostgreSQL Pod
                      │
                      ▼
             PersistentVolumeClaim
                      │
                      ▼
             Persistent Storage
```

### Kubernetes Storage Resources

The PostgreSQL deployment uses a PersistentVolumeClaim (PVC) to request persistent storage.

The storage is mounted into the PostgreSQL container and used for the PostgreSQL data directory.

### Storage Tasks Completed

- Created PostgreSQL persistent storage configuration
- Created a PersistentVolumeClaim
- Connected the PVC to the PostgreSQL workload
- Mounted the persistent storage into PostgreSQL
- Verified the PostgreSQL storage configuration

Using persistent storage prevents PostgreSQL data from depending only on the temporary filesystem of a pod.

## 📊 Monitoring & Observability

Monitoring was added to observe the Kubernetes environment and application infrastructure.

### Monitoring Stack

- Prometheus
- Grafana

### Monitoring Architecture

```text
Kubernetes Environment
         │
         ▼
     Prometheus
         │
         ▼
      Grafana
         │
         ▼
    Monitoring
   & Dashboards
```

### Monitoring Tasks Completed

- Configured Prometheus
- Configured Grafana
- Connected the monitoring components
- Collected Kubernetes/application metrics
- Used Grafana dashboards to visualize monitoring data
- Verified the monitoring setup

Monitoring provides visibility into the running environment and helps identify operational issues during deployment and troubleshooting.

## 🔐 Security & Secrets

Security practices were implemented to protect application credentials and restrict access to the infrastructure.

### AWS Security

AWS Security Groups were configured to control network access to the EC2 server.

The required ports were restricted to the configured client IP where applicable.

### Kubernetes Secrets

Sensitive application credentials were stored using Kubernetes Secrets instead of placing them directly inside application configuration.

The project uses Secrets for:

- PostgreSQL credentials
- Redis password

### Secret Usage

```text
Kubernetes Secret
       │
       ├── PostgreSQL
       │
       └── Redis
              │
              ├── Vote Application
              └── Worker
```

### Security Tasks Completed

- Configured AWS Security Group rules
- Restricted SSH access
- Configured application access through required ports
- Created PostgreSQL Kubernetes Secret
- Created Redis Kubernetes Secret
- Referenced Secrets from Kubernetes workloads
- Avoided storing sensitive credentials directly in application manifests

Secrets and sensitive configuration files are excluded from Git using `.gitignore`.

## 🤖 Full Automation

The project combines Terraform, Ansible, Kubernetes, and Python automation to reduce manual deployment and configuration steps.

### Automation Workflow

```text
Terraform
    │
    ▼
AWS Infrastructure
    │
    ▼
Ansible
    │
    ▼
Ubuntu Server Configuration
    │
    ▼
Docker Environment
    │
    ▼
Kubernetes
    │
    ▼
Application Deployment
    │
    ▼
Python Health Check
```

### Automation Components

| Tool | Automation Responsibility |
|---|---|
| Terraform | Provisions AWS infrastructure |
| Ansible | Configures the Linux server and deploys the Docker application |
| Kubernetes | Manages application workloads and services |
| Python | Performs Kubernetes health checks and automation |
| Docker Compose | Runs the application services together |

### Automation Tasks Completed

- Automated AWS infrastructure provisioning with Terraform
- Automated Linux server configuration with Ansible
- Automated Docker application deployment
- Automated Kubernetes application deployment
- Added Python-based Kubernetes health checking
- Used GitHub as the source repository for the deployment workflow

The project is designed so that infrastructure and application configuration can be reproduced from code instead of relying entirely on manual configuration.

## 🔄 Destroy & Rebuild

Terraform is used to manage the AWS infrastructure as code, allowing the environment to be destroyed and recreated from the project configuration.

### Rebuild Workflow

```text
Terraform Configuration
        │
        ▼
 terraform destroy
        │
        ▼
AWS Infrastructure Removed
        │
        ▼
 terraform apply
        │
        ▼
AWS Infrastructure Recreated
        │
        ▼
Ansible Configuration
        │
        ▼
Application Deployment
        │
        ▼
Verification
```

### Rebuild Objective

The goal of this phase is to verify that the infrastructure and deployment process are reproducible from code rather than depending on manually configured resources.

The rebuild process includes:

- Destroying Terraform-managed infrastructure
- Recreating the AWS infrastructure using Terraform
- Reconfiguring the server using Ansible
- Deploying the application
- Verifying the application and infrastructure

## 🛠️ Troubleshooting & Debugging

Troubleshooting was performed during the Kubernetes deployment to identify and resolve application communication and runtime issues.

### Major Issue Resolved

The Vote application initially returned an HTTP 500 error when submitting a vote.

The application logs showed a Redis authentication/protocol error:

```text
redis.exceptions.AuthenticationError:
HELLO must be called with the client already authenticated
```

### Troubleshooting Process

```text
Vote Application
       │
       ▼
HTTP 500 Error
       │
       ▼
Check Application Logs
       │
       ▼
Identify Redis Authentication Error
       │
       ▼
Investigate Redis Service
       │
       ▼
Verify Redis Password & Connectivity
       │
       ▼
Update Redis Client Configuration
       │
       ▼
Rebuild Docker Image
       │
       ▼
Reload Image into Kubernetes
       │
       ▼
Restart Deployment
       │
       ▼
Verify Vote → Redis → Worker → PostgreSQL
```

### Additional Verification

The troubleshooting process included:

- Inspecting Kubernetes pod logs
- Checking Kubernetes Services
- Verifying Redis connectivity
- Testing Redis commands from the Vote pod
- Checking Worker logs
- Rebuilding application Docker images
- Reloading updated images into Minikube
- Restarting Kubernetes deployments
- Verifying PostgreSQL records
- Testing the complete voting workflow

### Final Result

The complete application flow was successfully verified:

```text
User
 │
 ▼
Vote Application
 │
 ▼
Redis
 │
 ▼
Worker
 │
 ▼
PostgreSQL
 │
 ▼
Result Application
```

This troubleshooting process demonstrated practical debugging of containerized applications, Kubernetes networking, Redis communication, application logs, and database persistence.

