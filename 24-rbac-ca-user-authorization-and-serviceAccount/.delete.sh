#!/bin/bash

RESOURCES_PATH=./resources/

# kubectl delete -f "$RESOURCES_PATH"no-access-rolebinding.yaml
kubectl delete -f ${RESOURCES_PATH}role.yaml -f ${RESOURCES_PATH}rolebinding.yaml -f "$RESOURCES_PATH"pod.yaml