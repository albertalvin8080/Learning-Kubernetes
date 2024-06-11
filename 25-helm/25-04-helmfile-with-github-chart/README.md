## Testing Helmfile with helm-git plugin

1. Install helm-git plugin

   ```
   helm plugin install https://github.com/aslafy-z/helm-git --version 0.16.0
   ```

2. Create helmfile.yaml

   ```
   cat <<EOF > helmfile.yaml
   ---
   repositories:
     - name: spring-repo
       url: git+https://github.com/albertalvin8080/Learning-Kubernetes@25-helm/25-02-k8s-spring-hello?ref=main&sparse=0

     - name: hello-repo
       url: git+https://github.com/albertalvin8080/Learning-Kubernetes@25-helm/25-01-helloworld?ref=main&sparse=0
   releases:
     - name: spring
       namespace: spring-ns
       chart: spring-repo/k8sspringhello
       version: 0.1.0 # Refers to a property inside 'k8sspringhello/Chart.yaml'
       installed: true

     - name: helloworld
       namespace: default
       chart: hello-repo/helloworld
       version: 0.1.0
       installed: true
   EOF
   ```

3. Install the remote chart

   ```
   helmfile sync
   ```

4. List charts across all namespaces

   ```
   helm list -a -A
   ```

5. Find the services and it's ports and make a request to each one
   ```
   kubectl get svc -A
   ```
   ```
   curl localhost:<port>; echo
   ```
