#!/bin/sh

# Install python3 on Alpine linux (Docker)
if ! [ -v "$(command -v apk)" ]; then
  apk add python3
  exit 0
fi
# Install python 3 on Arch Linux (if already does not have)
if ! [ -v "$(command -v pacman)" ]; then
  pacman -S python
  exit 0
fi