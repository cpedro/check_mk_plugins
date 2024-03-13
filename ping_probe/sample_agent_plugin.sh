#!/bin/sh
#########################
# Assumes that the NMS Network Utilities is downloaded and installed into:
#   /opt/nms_net_utils
# AND JSON config file is located in:
#   /usr/lib/check_mk_agent/plugins/
#########################

cmd="/opt/nms_net_utils/cmk_ping_probe.py"
cfg="/usr/lib/check_mk_agent/plugins/ping_probe.json"

${cmd} ${cfg}
