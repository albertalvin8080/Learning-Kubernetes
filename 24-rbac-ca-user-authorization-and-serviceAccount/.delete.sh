#!/bin/bash

RESOURCES_PATH=./resources

# kubectl delete -f "$RESOURCES_PATH"/no-access-rolebinding.yaml
kubectl delete \
-f ${RESOURCES_PATH}/user-role.yaml \
-f ${RESOURCES_PATH}/user-rolebinding.yaml \
-f ${RESOURCES_PATH}/nginx-service-account.yaml \
-f "$RESOURCES_PATH"/pod.yaml