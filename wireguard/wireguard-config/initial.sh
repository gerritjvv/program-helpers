#!/bin/bash
# KEYS=[vpn wireguard install]

echo "# Installing Wireguard"
./install.sh
./add-client.sh
echo "# Wireguard installed"
