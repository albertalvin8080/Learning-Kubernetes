kubectl delete -f nginx-sts.yml 
kubectl delete pvc --all
@REM Yes, this should be here. If you try to delete the PC before the PVC, it will wait endlessy for the PVC to stop first.
kubectl delete -f pv.yml