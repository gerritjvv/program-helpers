#!/usr/bin/env bash

iwlist wlp3s0 scanning | grep Frequency | sort | uniq -c | sort -n