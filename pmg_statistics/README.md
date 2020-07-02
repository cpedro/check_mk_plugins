# Check_MK Plugin for Proxmox Mail Gateway Statistics

Along with the plugin agent, it will run `pmgsh get /statistics/mail` and
monitor the statistics reported back.


## Installation

For now, all you need to do to use this plugin is the following:

1. Copy `plugins/pmg_statistics.sh` to the Proxmox Mail Gateway server.  Put it
  in the plugin directory to be run by `check_mk_agent`.  In Linux, this
  directory is `/usr/lib/check_mk_agent/plugins`.
1. On the Check_MK server, copy the following files:
    * `checkman/pmg_statistics` to `${OMD_ROOT}/local/share/check_mk/checkman/`
    * `checks/pmg_statistics` to `${OMD_ROOT}/local/share/check_mk/checks/`
    * `web/plugins/*` to `${OMD_ROOT}/local/share/check_mk/web/plugins/`
1. Rescan you PMG server, and add the new metric.

