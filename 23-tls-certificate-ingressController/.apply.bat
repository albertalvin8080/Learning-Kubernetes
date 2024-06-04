echo Remember to run `minikube addons enable ingress` from a terminal with adm privilleges.
kubectl apply -f nginx-pod.yaml -f ingress.yaml