kubectl apply -f nginx-sts.yml
@REM # WARNING: if you apply the pv.yml, all pods will try to have a PVC fot the same PC. Because it's not allowed, only the first pod will be successfully deployed.
@REM kubectl apply -f pv.yml