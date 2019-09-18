#!/bin/bash

changed=false
swap=$(free | grep Swap | grep -E "[1-9]")
if [[ -n "${swap}" ]]; then
  swapoff -a
  changed=true
fi

if $changed; then
  exit 254
else
  exit 0
fi
