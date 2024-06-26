kubectl label namespace kube-system networking/namespace=kube-system
kubectl apply ^
    -f ns-backend.yaml ^
    -f ns-frontend.yaml ^
    -f ns-production.yaml ^
    -f nginx.yaml ^
    -f busybox.yaml ^
    -f spring.yaml 