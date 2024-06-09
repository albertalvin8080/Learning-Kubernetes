# Creating a custom User

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

# Creating a ServiceAccount for nginx pod

## Find the directory where the token is located. Generally it's located at:
### There you sould see three files: `ca.crt`, `namespace` and `token`
```bash
cd /var/run/secrets/kubernetes.io/serviceaccount
```

## Make a insecure request to the Kubernertes API
### You should receive a `forbidden 403` from the API.
```bash
curl -k https://kubernetes.default.svc/api/v1/namespaces/devinc/pods/
```

## Use the token to make a request to Kubernetes API

### Export the these variables for convenience
```bash
export SERVICEACCOUNT=/var/run/secrets/kubernetes.io/serviceaccount
export NAMESPACE=$(cat ${SERVICEACCOUNT}/namespace)
export TOKEN=$(cat ${SERVICEACCOUNT}/token)
export CACERT=${SERVICEACCOUNT}/ca.crt # Should be the path, not the content of the certificate.
export APISERVER=https://kubernetes.default.svc
```

### You should still receive a `forbidden 403`, but now specifying that the `default` ServiceAccount doesn't have permission to list the pods inside devinc namespace.
```bash
curl --cacert ${CACERT} \
--header "Authorization: Bearer $TOKEN" \
-s ${APISERVER}/api/v1/namespaces/${NAMESPACE}/pods/ 
```
