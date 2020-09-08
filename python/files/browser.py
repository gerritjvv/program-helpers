#!/usr/bin/env bash
# KEYS=[browser url open]

import webbrowser

websites = [
    'https://www.python.org/'
    ]

for website in websites:
    webbrowser.open_new(website)