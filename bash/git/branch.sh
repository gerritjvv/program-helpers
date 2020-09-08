#!/usr/bin/env bash
# branch helpers
# KEYS=[git branch name commit hash]

# branch name
git rev-parse --abbrev-ref HEAD
# commit short hash
git rev-parse --verify --short HEAD