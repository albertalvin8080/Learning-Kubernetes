## Downloading Helm 3.0 on WSL
```
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

## Create the hellowrld chart
```
helm create helloworld
```

## Check the validity of helloworld chart
```
helm install --debug --dry-run myhelloworld helloworld
```

## Install helloworld chart
```
helm install myhelloworld helloworld
```

## List all charts inside the cluster
```
helm list -a
```