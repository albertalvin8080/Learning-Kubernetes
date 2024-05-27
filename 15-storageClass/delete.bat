kubectl delete -f pod.yml --force --grace-period=0
kubectl delete -f pvc.yml -f sc.yml