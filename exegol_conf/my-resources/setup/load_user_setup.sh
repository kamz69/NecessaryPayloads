#!/bin/bash
set -e
tmux
#bash <(curl -L zellij.dev/launch)

# This script will be executed on the first startup of each new container with the "my-resources" feature enabled.
# Arbitrary code can be added in this file, in order to customize Exegol (dependency installation, configuration file copy, etc).
# It is strongly advised **not** to overwrite the configuration files provided by exegol (e.g. /root/.zshrc, /opt/.exegol_aliases, ...), official updates will not be applied otherwise.

# Exegol also features a set of supported customization a user can make.
# The /opt/supported_setups.md file lists the supported configurations that can be made easily.

#install wine tool apt
sudo mkdir -pm755 /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/bookworm/winehq-bookworm.sources
sudo apt update
sudo apt install --install-recommends winehq-stable
