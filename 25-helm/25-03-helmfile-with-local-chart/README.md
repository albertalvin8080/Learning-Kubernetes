## Testing Helmfile on WSL

1. Download Helmfile

   > Note: Use`uname -u` in order to get your WSL archtecture. Also, _86x_64_ stands for _amd64_.

   ```
   curl -fSLO https://github.com/roboll/helmfile/releases/download/v0.144.0/helmfile_linux_amd64 && \
   sudo mv helmfile_linux_amd64 /usr/local/bin/helmfile && \
   chmod 755 /usr/local/bin/helmfile
   ```

2. Create a helm chart

   ```
   helm create helloworld
   ```

3. Create helmfile.yaml and populate it

   ```
   cat <<EOF > helmfile.yaml
   ---
   releases:
     - name: helloworld
       chart: ./helloworld
       installed: true
   EOF
   ```

4. Install the chart using `helmfile sync`

   ```
   helmfile sync
   ```

5. Check it

   ```
   helm list -a
   ```

6. Change `releases.installed` to `false` inside helmfile.yaml

   ```
   cat <<EOF > helmfile.yaml
   ---
   releases:
     - name: helloworld
       chart: ./helloworld
       installed: false
   EOF
   ```

7. Use `helmfile sync` again to uninstall the chart

   ```
   helmfile sync
   ```

