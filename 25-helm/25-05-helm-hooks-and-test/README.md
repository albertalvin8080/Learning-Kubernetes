# Testing Helm Hooks (Helm Test is a type of Hook)

## Helm Hooks

1. Create a new chart

   ```
    helm create helloworld
   ```

1. Create a folder for the hooks

   ```
   mkdir helloworld/templates/hooks
   ```

1. Create copy `pre-install.yaml` to the hooks folder

   ```
   cp pre-install.yaml helloworld/templates/hooks
   ```

1. Watch for all pods

   ```
   watch -x kubectl get pods
   ```

1. Install the chart

   ```
   helm instal mychart helloworld
   ```

1. See the logs inside the Pod created by the Job (you must be fast in order to see it)

   ```
   kubectl logs <pod-name>
   ```

1. Use the default test provided by helloworld

   ```
   helm test mychart
   ```

1. Uninstall the chart
   ```
   helm uninstall mychart
   ```

## Helm Test

   > Note: `deployment.yaml` and `test-file-existence.yaml` were edited to use the same PersistentVolumeClaim. That's why both of them can see the content of /www/test/ mountPath.

   > Note: *volume* and *volumeMounts* properties were edited inside `values.yaml`. You could also simply change them directly inside `deployment.yaml` and `test-file-existence.yaml`, but then you would not be using helm-template.

1. Copy `deployment.yaml` to helloworld/templates/

   ```
   cp deployment.yaml helloworld/templates
   ```

1. Copy `test-file-existence.yaml` to /helloworld/templates/tests

   ```
   cp test-file-existence.yaml /helloworld/templates/tests
   ```

1. Remove `test-connection.yaml` (it would fail because `deployment.yaml` is not using nginx anymore)

   ```
   rm helloworld/templates/tests/test-connection.yaml
   ```

1. Install the chart again

   ```
   helm install mychart helloworld
   ```

1. Run the tests

   ```
   helm test mychart
   ```

1. Uninstall the chart
   ```
   helm uninstall mychart
   ```
