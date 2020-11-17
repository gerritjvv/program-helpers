#!/usr/bin/env python3
# KEY = [python command shell process]
import subprocess


def sh(cmd):
    out = subprocess.check_output([cmd], shell=True)
    return out