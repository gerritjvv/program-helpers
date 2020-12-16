# KEYS = [kubernetes k8s force deploy redeploy rolling restart]
#!/usr/bin/env bash


NS="$1"
DEPLOYMENT="$2"


if [ -z "$DEPLOYMENT" ];
then

  echo "$0 [namespace] [deployment]"
  exit -1

fi

kubectl -n "$NS" patch deployment "$DEPLOYMENT" -p "{\"spec\": {\"template\": {\"metadata\": { \"labels\": {  \"redeploy\": \"$(date +%s)\"}}}}}"

