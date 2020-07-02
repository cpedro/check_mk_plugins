# Check_MK Plugin for Proxmox Virtual Environment QEMU VMs

Along with the plugin agent, it will run `qm list` to get status of each QEMU
VM running on the system and monitor it.

Adapted from code found on the
[PVE doc page](https://pve.proxmox.com/wiki/Nagios_check_mk).

## Installation

For now, all you need to do to use this plugin is the following:

1. Copy `plugins/pve_qemu.sh` to the Proxmox Virtual Environment server.  Put it
  in the plugin directory to be run by `check_mk_agent`.  In Linux, this
  directory is `/usr/lib/check_mk_agent/plugins`.
1. On the Check_MK server, copy the following files:
    * `checkman/*` to `${OMD_ROOT}/local/share/check_mk/checkman/`
    * `checks/*` to `${OMD_ROOT}/local/share/check_mk/checks/`
    * `web/plugins/*` to `${OMD_ROOT}/local/share/check_mk/web/plugins/`
1. Rescan you PVE server, and add the new metric.

