#!/bin/bash
#/usr/lib/check_mk_agent/plugins

# Monitor Proxmox Mail Gateway Statistics
#
# Author: Chris Pedro
# Date: 2020-06-25

if which pmgsh >/dev/null; then
  for stats in mail; do
    echo "<<<pmg_statistics>>>"
    echo "[[[${stats}]]]"
    pmgsh get /statistics/${stats} 2>&1 | while read line; do
      if [[ ! -z $line ]]; then
        if [[ $line =~ ^([0-9]{3})[[:space:]](.*)$ ]]; then
          [[ ${BASH_REMATCH[1]} -eq 200 ]] || break
        else
          echo "${line}"
        fi
      fi
    done
  done
fi
