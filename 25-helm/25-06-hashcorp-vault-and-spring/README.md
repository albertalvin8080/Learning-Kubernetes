## Testing HashCorp Vault with Spring-Boot

1. Enable the default _hostpath storage_ if you're using Microk8s

   ```
   microk8s enable hostpath-storage
   ```

1. Add [hashcorp repo](https://artifacthub.io/packages/helm/hashicorp/vault) to your helm client

   ```
   helm repo add hashicorp https://helm.releases.hashicorp.com
   ```

1. Install the Vault

   ```
   helm install my-vault hashicorp/vault --namespace vault --create-namespace
   ```

1. Forward the pod which contains the Vault

   > Note: Remember to kill the background process afterwards. Use `ps` to see the processes that are associated with the terminal you’re currently using and `kill <PID> <PID>` to kill them.

   ```
   (kubectl port-forward -n vault my-vault-0 8200:8200 &> port-forward.txt &)
   ```

1. If you're using WSL, you need to forward another port to Windows

   > Note: For accessing the vault Pod from Windows, you must use the ip of the WSL VM and the forwarded port (8100 in this case). <br>
   > Ex: http://172.29.156.149:8100/

   > WARNING: Remember to annotate the Unseal Keys and the Root Key which HashCorp provides in the first login. You can also download them as a JSON from the same page.

   ```
   socat TCP-LISTEN:8100,fork TCP:localhost:8200 &
   ```

1. Unseal, access and then add a Username and a Password secret to the Vault inside kv/spring

1. Run the Spring app locally and watch for the logging of the secrets you defined inside kv/spring

   > Note: You may need to change the application.yaml being used, or just use SPRING_PROFILES_ACTIVE

   ```
   cd spring-hashcorp-test && \
   mvn clean install -DskipTests && \
   java -jar target/spring-hashcorp-test-0.0.1-SNAPSHOT.jar && \
   cd ..
   ```

1. Enter the Pod which contains the Vault and enable authentication using Kubernetes

   ```
   kubectl exec -it -n vault my-vault-0 -- sh
   ```

   > Note: You need to provide the root token to log in

   ```
   vault login
   ```

   > Note: The Kubernetes CA (ca.crt) is automatically configured into the Vault when using `vault write` command.

   ```
   vault auth enable kubernetes && \
   vault write auth/kubernetes/config kubernetes_host=https://$KUBERNETES_SERVICE_HOST:$KUBERNETES_SERVICE_PORT
   ```

1. Check the folder containing **ca.crt**, **token**, and **namespace** files

   ```
   ls -l /var/run/secrets/kubernetes.io/serviceaccount/
   ```

1. Add a Policy through thre browser interface

1. Add a Role through the browser interface (don't forget to use the same namespace used for the resources) and link it with the Policy created in the previous step

1. Apply `spring-pod.yaml` for it contains the image of the Spring app

   ```
   kubectl create namespace app
   ```

   ```
   kubectl apply -f spring-pod.yaml
   ```

1. Check the logs of the created Pod and search for printed Username and Password secrets
