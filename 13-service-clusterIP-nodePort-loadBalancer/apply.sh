#!/bin/bash

echo -e "Choose a type for the Service:\n1) ClusterIP\n2) NodePort\n3) LoadBalancer"
read -p "?:" type

echo
if [ "$type" == "1" ]; then
    kubectl apply -f service-clusterip.yml
elif [ "$type" == "2" ]; then
    kubectl apply -f service-nodeport.yml
elif [ "$type" == "3" ]; then
    kubectl apply -f service-loadbalancer.yml
else
    echo "Invalid Choice."
    read -p "Press any key to close..."
    exit 1
fi

kubectl apply -f busybox-pod.yml -f nginx-pod.yml

echo
read -p "Press any key to close..."
