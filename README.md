# 🗳️ Project 3 — Cloud-Native Voting App Automation

A DevOps and cloud-native project focused on automating the deployment and management of a distributed voting application.

## 📌 Project Overview

This project uses an existing distributed voting application and builds a complete DevOps deployment workflow around it.

The application consists of:

- Python Vote application
- Node.js Result application
- .NET Worker
- Redis
- PostgreSQL

The project will progressively move from local Docker-based execution to an automated cloud-native deployment.

## 🏗️ Current Application Architecture

```text
                    User
                  /      \
                 ▼        ▼
           Vote App    Result App
              │            ▲
              ▼            │
            Redis          │
              │            │
              ▼            │
            Worker         │
              │            │
              ▼            │
         PostgreSQL ───────┘

```

## 🛠️ Technologies

Currently used in the application:

- Python
- Node.js
- .NET
- Redis
- PostgreSQL
- Docker
- Docker Compose

Planned DevOps technologies:

- Git & GitHub
- Linux
- Terraform
- Ansible
- Kubernetes
- Kubernetes Ingress
- Prometheus
- Grafana
- Python automation
- AWS

## 📊 Current Status

### Phase 1 — Existing Voting Application

- [x] Clone existing voting application
- [x] Run application locally
- [x] Verify Vote application
- [x] Verify Result application
- [x] Verify complete voting flow
- [x] Understand application services
- [x] Inspect Docker Compose configuration
- [x] Inspect existing Kubernetes specifications

### Phase 2 — Git & Project Structure

- [x] Create Project 3 directory
- [x] Create project structure
- [x] Initialize Git repository
- [x] Create `.gitignore`
- [x] Create initial Git commit
- [x] Create GitHub repository
- [x] Push project to GitHub
- [ ] Complete repository organization

**Project Status:** 🚧 In Progress

