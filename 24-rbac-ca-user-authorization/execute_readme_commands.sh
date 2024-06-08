#!/bin/bash

# WARNING: this script assumes you're using microk8s snap with wsl
echo

rm -rf ./cert.d
mkdir ./cert.d
cp /var/snap/microk8s/current/certs/ca.crt ./cert.d/ca.crt
cp /var/snap/microk8s/current/certs/ca.key ./cert.d/ca.key

python3 .generate_user_certificate.py

export KUBECONFIG=~/.kube/customconfig

echo -e '\033[0;31m'Remember to confirm the Kubernetes Server IP for the cluster field.'\033[0m'
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

echo -e "\n\033[0;36mStep 3: List roles, role bindings, cluster roles and cluster role bindings in devinc namespace\033[0m"
kubectl get roles,rolebindings,clusterrole,clusterrolebindings -n devinc

echo -e "\n\033[0;36mStep 4: Attempt to list pods (expecting forbidden error)\033[0m"
kubectl get pods

echo -e "\n\033[33mWARNING:\nIf you're not seeing the 'forbidden' error, it may be due to already existing clusterrolebindings. In this case, you may want to explicitly create a roleBinding with no permissions for the devinc namespace.\033[0m\n"