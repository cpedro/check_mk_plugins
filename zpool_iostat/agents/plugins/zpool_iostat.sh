#!/bin/bash
#/usr/lib/check_mk_agent/plugins

# Monitor Zpool iostat
# Author: Chris Pedro
# Date: 2024-02-27

if which zpool >/dev/null ; then
  echo '<<<zpool_iostat>>>'
  zpool iostat -Hylp 1 1 | sed 's/-/0/g;s/\t\+/\ /g'
fi

