## Start Minikube
```bash
minikube start --driver=hyperv --cpus=4 --memory=3000
```

## Start Nginx implementation of Ingress Controller
```bash
minikube addons enable ingress
```

## Verify existence of ingress-nginx-controller-*
```bash
kubectl get pod -n ingress-nginx
```