#!/bin/bash

# PATH=./resources/ # Ah yes, such a nice idea: overriding the PATH variable (yes, it's sarcasm).
RESOURCES_PATH=./resources/

# kubectl apply -f ${RESOURCES_PATH}no-access-rolebinding.yaml
kubectl apply -f ${RESOURCES_PATH}role.yaml -f ${RESOURCES_PATH}rolebinding.yaml -f "$RESOURCES_PATH"pod.yaml