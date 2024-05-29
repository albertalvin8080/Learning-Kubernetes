kubectl create namespace frontend
kubectl create namespace backend
kubectl apply -f nginx.yaml -f busybox.yaml