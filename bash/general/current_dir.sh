#!/usr/bin/env bash
# KEYS = [bash current dir directory path]

# dir is the directory of the script ./current_dir.sh
dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

echo "$dir"