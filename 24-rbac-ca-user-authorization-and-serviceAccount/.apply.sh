#!/bin/bash

# PATH=./resources # Ah yes, such a nice idea: overriding the PATH variable (yes, it's sarcasm).
RESOURCES_PATH=./resources

# kubectl apply -f ${RESOURCES_PATH}/no-access-rolebinding.yaml
kubectl apply \
-f ${RESOURCES_PATH}/user-role.yaml \
-f ${RESOURCES_PATH}/user-rolebinding.yaml \
-f ${RESOURCES_PATH}/nginx-service-account.yaml \
-f "$RESOURCES_PATH"/pod.yaml 