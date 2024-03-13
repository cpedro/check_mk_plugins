# Check_MK Plugin for Ping Probes

This plugin will gather ping outputs from the remote agent and report back on
packet loss, latency, jitter and calculated MOS score to specific destinations.

## Installation

For now, all you need to do to use this plugin is the following:

1. Download and install the
  [NMS Network Utilities](https://github.com/cpedro/nms_net_utils) on the
  remote agent.  You will need to write your own script and put it in
  `/usr/lib/check_mk_agent/plugins` on the agent server which will run the
  Python script with JSON file.  I've provided a sample you can edit,
  `sample_agent_plugin.sh`
1. On the Check_MK server, copy the following files:
    * `checkman/*` to `${OMD_ROOT}/local/share/check_mk/checkman/`
    * `checks/*` to `${OMD_ROOT}/local/share/check_mk/checks/`
    * `web/plugins/*` to `${OMD_ROOT}/local/share/check_mk/web/plugins/`
1. Rescan you server, and add the new metric.
