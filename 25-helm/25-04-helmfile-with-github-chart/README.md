## Testing Helmfile

1. Install helm-git plugin

   ```
   helm plugin install https://github.com/aslafy-z/helm-git --version 0.16.0
   ```

2. Create helmfile.yaml

   ```
   cat <<EOF > helmfile.yaml
   ---
   repositories:
     - name: myrepo
       url: git+https://github.com/albertalvin8080/Learning-Kubernetes@25-helm/25-02-k8s-spring-hello/k8sspringhello?ref=main&sparse=0
   releases:
     - name: spring
       chart: myrepo/k8sspringhello
       installed: false
   EOF
   ```
