#!/usr/bin/env bash
# KEYS=[bash prod variables]


# take any var with a PROD prefix,
# removes the prefix and export it
# e.g PROD_DB=abc
#     becomes DB=abc in the current environment

config-prod () {
    for v in $(env | awk '/PROD_/ {gsub(/PROD_/,""); print $1}'); do
     eval "export $v"
    done
}