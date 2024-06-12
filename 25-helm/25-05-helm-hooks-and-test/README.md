# Testing Helm Hooks (Helm Test is a type of Hook)

## Helm Hooks

1. Create any chart

   ```
    helm create helloworld
   ```

2. Create a folder for the hooks

   ```
   mkdir helloworld/templates/hooks
   ```

3. Create copy the pre-install.yaml to the hooks folder

   ```
   cp pre-install.yaml helloworld/templates/hooks
   ```

4. Watch for all pods

   ```
   watch -x kubectl get pods
   ```

5. Install the chart

   ```
   helm instal mychart helloworld
   ```

6. See the logs inside the Pod created by the Job (you must be fast in order to see it)

   ```
   kubectl logs <pod-name>
   ```

7. Uninstall the chart
   ```
   helm uninstall mychart
   ```

## Helm Test
