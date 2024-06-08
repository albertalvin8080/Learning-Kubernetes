## Copy Kubernetes CA to cert.d/
```bash
rm -rf ./cert.d && \
mkdir ./cert.d && \
cp /var/snap/microk8s/current/certs/ca.crt ./cert.d/ca.crt && \
cp /var/snap/microk8s/current/certs/ca.key ./cert.d/ca.key
```

## Generate user crt and key:
```bash
python3 .generate_user_certificate.py
```

## Export the new kubeconfig file
```bash
export KUBECONFIG=~/.kube/customconfig
```

### Do this to go back to the original kubeconfig
```bash
export KUBECONFIG=~/.kube/config
```

## Fill the custom kubeconfig file
### 1. Set the cluster
Change the value of `--server` to your actual Kubernetes Cluster's IP
```bash
kubectl config set-cluster test-cluster \
--server=https://172.29.156.149:16443 \
--certificate-authority=./cert.d/ca.crt \
--embed-certs=true
```

### 2. Set the user
```bash
kubectl config set-credentials albert \
--client-certificate=./cert.d/albert.crt \
--client-key=./cert.d/albert.key \
--embed-certs=true
```

### 3. Set the context
```bash
kubectl config set-context test-ctx \
--cluster=test-cluster \
--namespace=devinc \
--user=albert
```
```bash
kubectl config use-context test-ctx
```

