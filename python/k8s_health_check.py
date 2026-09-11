from kubernetes import client, config
import sys

# Load Kubernetes configuration
config.load_kube_config()

# Create Kubernetes API clients
v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()

# Namespace to monitor
NAMESPACE = "project3"
all_healthy = True


# ============================================================
# POD HEALTH CHECK
# ============================================================

print("\n========== POD HEALTH ==========\n")
print(f"Namespace: {NAMESPACE}\n")

pods = v1.list_namespaced_pod(NAMESPACE)

for pod in pods.items:
    pod_name = pod.metadata.name
    pod_phase = pod.status.phase

    # Check Ready condition
    ready = False

    if pod.status.conditions:
        for condition in pod.status.conditions:
            if condition.type == "Ready":
                ready = condition.status == "True"

    # Determine pod health
    if pod_phase == "Running" and ready:
        health = "HEALTHY"
    else:
        health = "UNHEALTHY"
        all_healthy = False

    print(f"Pod:    {pod_name}")
    print(f"Status: {pod_phase}")
    print(f"Ready:  {ready}")
    print(f"Health: {health}")
    print("-" * 40)


# ============================================================
# DEPLOYMENT HEALTH CHECK
# ============================================================

print("\n========== DEPLOYMENT HEALTH ==========\n")

deployments = apps_v1.list_namespaced_deployment(NAMESPACE)

for deployment in deployments.items:
    deployment_name = deployment.metadata.name

    desired = deployment.spec.replicas or 0
    ready = deployment.status.ready_replicas or 0
    available = deployment.status.available_replicas or 0

    if ready == desired and available == desired:
        health = "HEALTHY"
    else:
        health = "UNHEALTHY"
        all_healthy = False

    print(f"Deployment: {deployment_name}")
    print(f"Desired:    {desired}")
    print(f"Ready:      {ready}")
    print(f"Available:  {available}")
    print(f"Health:     {health}")
    print("-" * 40)


# ============================================================
# FINAL RESULT
# ============================================================

if all_healthy:
    print("\nAll Kubernetes resources are healthy.")
    sys.exit(0)
else:
    print("\nOne or more Kubernetes resources are unhealthy.")
    sys.exit(1)
