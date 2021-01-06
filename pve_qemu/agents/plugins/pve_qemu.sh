#!/bin/bash
#/usr/lib/check_mk_agent/plugins

# Monitor Proxmox QEMU VMs
# Author: Chris Pedro
# Date: 2020-07-01
# Original code: https://pve.proxmox.com/wiki/Nagios_check_mk

if which qm >/dev/null ; then
  echo '<<<pve_qemu>>>'
  qm list | tail -n +2 | while read line; do
    if [[ ! -z $line ]]; then
      id=$(echo $line | awk '{print $1}')
      xname=$(echo $line | awk '{$1=$NF=$(NF-1)=$(NF-2)=$(NF-3)="";print $0}')
      name=$(echo $xname | sed 's/ /_/g')
      state=$(echo $line | awk '{print $(NF-3)}')
      amem=$(echo $line | awk '{print $(NF-2)}')
      pid=$(echo $line | awk '{print $NF}')
      if [[ ! -z $pid ]] && [ "$pid" -gt "0" ]; then
        ps=$(ps aux | awk -v pid="$pid" '{if ($2 == pid) print}')
        vsz=$(echo $ps | awk -- '{print $5}')
        rss=$(echo $ps | awk -- '{print $6}')
        pmem=$(echo "scale=1; 100 * $rss / $vsz" | bc)
        data=$(top -p $pid -n 1 -b | tail -1)
        pcpu=$(echo $data | awk -- '{print $9}' | tr , .)
        mcpu=$(echo $ps | sed 's/.*maxcpus=\([^ ]*\)\ .*/\1/' )
        rcpu=$(echo "scale=1; $pcpu / $mcpu" | bc)
      else
        rcpu=""
        pmem=""
      fi
      echo "$id $name $state $amem $rcpu $pmem"
    fi
  done
fi

