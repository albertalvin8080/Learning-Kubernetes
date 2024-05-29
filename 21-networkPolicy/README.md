## Start your Minikube cluster with one control plane node using the following command (you must be logged in as adm):
```bash
minikube start --network-plugin=cni --cni=calico --driver=hyperv --cpus=4
```

##  Minikube automatically downloads and installs the Calico CNI plugin for you. However, if you want to customize your CNI Calico installation, you can do this:
```bash
 curl -L -A "Mozilla/5.0" -o calico.yaml https://raw.githubusercontent.com/projectcalico/calico/v3.28.0/manifests/calico.yaml
```
```bash
kubectl apply -f calico.yaml
```

## Verify Calico installation:
```bash
watch kubectl get pods -l k8s-app=calico-node -A
```