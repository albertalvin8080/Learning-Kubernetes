## Testing Helm 3.0 on WSL

1. Download Helm 3.0 on WSL

   ```sh
   curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 &&
   chmod 700 get_helm.sh &&
   ./get_helm.sh
   ```

2. Create the helloworld chart

   > Note:
   > If Helm throws warnings about group and world readability of kubeconfig file, just do a `chmod 700 /path/to/.kube/config`

   ```sh
   helm create helloworld
   ```

3. Validate the syntax of helm templates

   ```sh
   helm lint helloworld
   ```

4. Check the validity of helloworld chart locally

   ```sh
   helm template helloworld
   ```

5. Check the validity of helloworld chart against Kubernetes

   ```sh
   helm install --debug --dry-run myhelloworld helloworld
   ```

6. Install helloworld chart

   ```sh
   helm install myhelloworld helloworld
   ```

7. List all charts inside the cluster

   ```sh
   helm list -a
   ```

8. Change the Service Type to NodePort inside values.yaml

   ```sh
   nano helloworld/values.yaml
   ```

9. Upgrade helloworld chart

   ```sh
   helm upgrade myhelloworld helloworld
   ```

10. Get the port exposed by the service and make a request to it

    > Note:
    > You could also get the IP of WSL VM with `hostname -I` or `ip addr` and use it with the service port to directly make a request to the service from Windows.

    ```sh
    kubectl get svc
    curl localhost:<port>
    ```

11. Rollback helloworld chart

    ```sh
    helm rollback myhelloworld 1
    ```

12. Uninstall helloworld chart

    ```sh
    helm uninstall myhelloworld
    ```
