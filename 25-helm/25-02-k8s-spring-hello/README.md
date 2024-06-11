## Testing k8s-spring-hello

1. Inside `values.yaml`

   - Change the value of `image.repository` to **albertalvin/k8s-spring-hello**
   - Change the value of `image.tag` to **"0.0.6-SNAPSHOT"**
   - Change the service type to **NodePort**

2. Inside `templates/deployment.yaml`

   - Remove `spec.template.spec.containers.livenessProble` and `spec.template.spec.containers.livenessreadinessProbeProble`

3. Install the chart

   ```
   helm install spring k8sspringhello
   ```

4. Get the port attached to the service

   ```
   kubectl get svc
   ```

5. Make a request to the service

   ```
   curl localhost:<port>; echo
   ```

6. Again inside `values.yaml`

   - Change the value of `image.tag` to **"0.0.2-SNAPSHOT"**

7. Upgrade the chart

   ```
   helm upgrade spring k8sspringhello
   ```

8. Make a new request to the service

   ```
   curl localhost:<port>; echo
   ```
