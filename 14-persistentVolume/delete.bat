@REM This should come first, or else the PVC and PV will wait forever for deletion.
kubectl delete -f pod.yaml -f pod2.yaml --force --grace-period=0
kubectl delete -f pv.yaml -f pvc.yaml 