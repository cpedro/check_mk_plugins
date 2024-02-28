# Check_MK Plugin for ZFS Zpool Statistics

This will gather and graph zpool statistics, IOPS, bandwidth, latency, etc.

## Installation

For now, all you need to do to use this plugin is the following:

1. Copy `plugins/zpool_stats.sh` to the Proxmox Virtual Environment server.  Put it
  in the plugin directory to be run by `check_mk_agent`.  In Linux, this
  directory is `/usr/lib/check_mk_agent/plugins`.
1. On the Check_MK server, copy the following files:
    * `checkman/*` to `${OMD_ROOT}/local/share/check_mk/checkman/`
    * `checks/*` to `${OMD_ROOT}/local/share/check_mk/checks/`
    * `web/plugins/*` to `${OMD_ROOT}/local/share/check_mk/web/plugins/`
1. Rescan you server, and add the new metric.

