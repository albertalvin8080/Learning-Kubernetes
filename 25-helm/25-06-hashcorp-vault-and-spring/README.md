## Testing HashCorp Vault with Spring-Boot

1. Enable default _hostpath storage_ if you're using Microk8s

   ```
   microk8s enable hostpath-storage
   ```

1. Add [hashcorp](https://artifacthub.io/packages/helm/hashicorp/vault) repo to your helm client

   ```
   helm repo add hashicorp https://helm.releases.hashicorp.com
   ```

1. Install the Vault

   ```
   helm install my-vault hashicorp/vault --namespace vault --create-namespace
   ```

1. Forward the pod which contains the Vault

   ```
   kubectl port-forward -n vault my-vault-0 8200:8200
   ```

1. If you're using WSL, you need to forward another port to Windows

   > Note: For accessing the vault Pod from Windows, you must use the ip of the WSL VM and the forwarded port (8100 in this case). <br>
   > Ex: http://172.29.156.149:8100/

   > WARNING: Remember to annotate the Unseal Keys and the Root Key which HashCorp provides in the first login. You can also download them as a JSON from the same page.

   ```
   socat TCP-LISTEN:8100,fork TCP:localhost:8200
   ```

1. Unseal and then access the vault

1. Run the Spring app locally, access the env endpoint and search for the secrets you defined inside kv/spring
   ```
   http://localhost:8080/actuator/env
   ```