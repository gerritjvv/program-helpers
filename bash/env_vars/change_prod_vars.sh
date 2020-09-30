#!/usr/bin/env bash
# KEYS=[bash prod variables]

# Usage: . ./build.sh config-prod # keep the extra .
# take any var with a PROD prefix,
# removes the prefix and export it
# e.g PROD_DB=abc
#     becomes DB=abc in the current environment

config-prod () {
    for v in $(env | awk '/PROD_/ {gsub(/PROD_/,""); print $1}'); do
     eval "export $v"
    done
}


CMD="$1"
shift

case "$CMD" in
  config-prod )
    config-prod
    ;;
  * )
    echo "$0 config-prod"
    ;;
esac