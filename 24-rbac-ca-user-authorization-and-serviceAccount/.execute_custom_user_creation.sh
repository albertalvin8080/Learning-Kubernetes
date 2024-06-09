#!/bin/bash

# WARNING: this script assumes you're using microk8s snap with wsl
echo

# If you don't enable this before executing the rest of the script, you may need to reinstall your microk8s. Yes, it's that serious. Enabling and Disabling your RBAC configuration for your Cluster can break it.
microk8s enable rbac

rm -rf ./cert.d
mkdir ./cert.d
cp /var/snap/microk8s/current/certs/ca.crt ./cert.d/ca.crt
cp /var/snap/microk8s/current/certs/ca.key ./cert.d/ca.key

python3 .generate_user_certificate.py

kubectl create namespace devinc

# If this file doesn't exist, kubectl will create it for you.
export KUBECONFIG=~/.kube/customconfig

echo -e "\033[0;33mWARNING: Remember to confirm the Kubernetes Server IP for the cluster field.\033[0m"
kubectl config set-cluster test-cluster \
--server=https://172.29.156.149:16443 \
--certificate-authority=./cert.d/ca.crt \
--embed-certs=true 

kubectl config set-credentials albert \
--client-certificate=./cert.d/albert.crt \
--client-key=./cert.d/albert.key \
--embed-certs=true

kubectl config set-context test-ctx \
--cluster=test-cluster \
--namespace=devinc \
--user=albert

kubectl config use-context test-ctx

echo -e "\n---------- DEBUG ----------"
echo -e "\n\033[0;36mStep 1: Verify the kubeconfig\033[0m"
kubectl config view --minify

echo -e "\n\033[0;36mStep 2: Check current context\033[0m"
kubectl config current-context

# echo -e "\n\033[0;36mStep 3: List roles, role bindings, cluster roles and cluster role bindings in devinc namespace\033[0m"
# kubectl get roles,rolebindings,clusterrole,clusterrolebindings -n devinc

echo -e "\n\033[0;36mStep 4: Attempt to list pods (expecting forbidden error)\033[0m"
kubectl get pods

echo -e "\033[33mWARNING: If you're not seeing the 'forbidden' error:\nCase 1 - You forgot to enable RBAC configuration for your Cluster.\nCase 2 - You have already created roles and rolebindings for the user.\033[0m\n"

echo -e "\033[0;31mWARNING: The configuration set by 'export KUBECONFIG=~/.kube/customconfig' is only valid for this instance of the shell. You need to manually set the env var if you want to access the Cluster using the customconfig file from another instance.\n"