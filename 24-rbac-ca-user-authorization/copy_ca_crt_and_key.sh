#!/bin/bash

# WARNING: this script assumes you're using microk8s snap with wsl

mkdir ./cert.d
cp /var/snap/microk8s/current/certs/ca.crt ./cert.d/ca.crt
cp /var/snap/microk8s/current/certs/ca.key ./cert.d/ca.key