#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# This file is part of the Proxmox Virtual Environment for Check_MK
# It defines metric information used in the plugin.
# Author: Chris Pedro
# Date: 2020-07-01


#   .--Checks--------------------------------------------------------------.
#   |                    ____ _               _                            |
#   |                   / ___| |__   ___  ___| | _____                     |
#   |                  | |   | '_ \ / _ \/ __| |/ / __|                    |
#   |                  | |___| | | |  __/ (__|   <\__ \                    |
#   |                   \____|_| |_|\___|\___|_|\_\___/                    |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  How various checks' performance data translate into the known       |
#   |  metrics                                                             |
#   '----------------------------------------------------------------------'

check_metrics['check_mk-pve_qemu'] = {  # noqa: F821
    'cpu': {'name': 'pve_cpu', },
    'memory_current': {'name': 'pve_memory_current', },
    'memory_assigned': {'name': 'pve_memory_assigned', },
}


#   .--Metrics-------------------------------------------------------------.
#   |                   __  __      _        _                             |
#   |                  |  \/  | ___| |_ _ __(_) ___ ___                    |
#   |                  | |\/| |/ _ \ __| '__| |/ __/ __|                   |
#   |                  | |  | |  __/ |_| |  | | (__\__ \                   |
#   |                  |_|  |_|\___|\__|_|  |_|\___|___/                   |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Definitions of metrics                                              |
#   '----------------------------------------------------------------------'

# From indexed_color() in cmk/gui/plugins/metrics/utils.py
# Colors:
#
#                   red
#  magenta                       orange
#            11 12 13 14 15 16
#         46                   21
#         45                   22
#   blue  44                   23  yellow
#         43                   24
#         42                   25
#         41                   26
#            36 35 34 33 32 31
#     cyan                       yellow-green
#                  green
#
# Special colors:
# 51  gray
# 52  brown 1
# 53  brown 2

metric_info['pve_cpu'] = {  # noqa: F821
    'title': _('CPU Usage'),  # noqa: F821
    'unit': '%',
    'color': '41/a',
}

metric_info['pve_memory_current'] = {  # noqa: F821
    'title': _('Memory Usage'),  # noqa: F821
    'unit': '%',
    'color': '33/a',
}

metric_info['pve_memory_assigned'] = {  # noqa: F821
    'title': _('Assigned Memory'),  # noqa: F821
    'unit': 'bytes',
    'color': '31/a',
}


#   .--Perf-O-Meters-------------------------------------------------------.
#   |  ____            __        ___        __  __      _                  |
#   | |  _ \ ___ _ __ / _|      / _ \      |  \/  | ___| |_ ___ _ __ ___   |
#   | | |_) / _ \ '__| |_ _____| | | |_____| |\/| |/ _ \ __/ _ \ '__/ __|  |
#   | |  __/  __/ |  |  _|_____| |_| |_____| |  | |  __/ ||  __/ |  \__ \  |
#   | |_|   \___|_|  |_|        \___/      |_|  |_|\___|\__\___|_|  |___/  |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Definition of Perf-O-Meters                                         |
#   '----------------------------------------------------------------------'

perfometer_info.append({  # noqa: F821
    "type": "stacked",
    "perfometers": [
        {
            "type": "linear",
            "segments": ["pve_cpu"],
            "total": 100.0,
        },
        {
            "type": "linear",
            "segments": ["pve_memory_current"],
            "total": 100.0,
        }
    ],
})


#   .--Graphs--------------------------------------------------------------.
#   |                    ____                 _                            |
#   |                   / ___|_ __ __ _ _ __ | |__  ___                    |
#   |                  | |  _| '__/ _` | '_ \| '_ \/ __|                   |
#   |                  | |_| | | | (_| | |_) | | | \__ \                   |
#   |                   \____|_|  \__,_| .__/|_| |_|___/                   |
#   |                                  |_|                                 |
#   +----------------------------------------------------------------------+
#   |  Definitions of time series graphs                                   |
#   '----------------------------------------------------------------------'

graph_info['pve_cpu'] = {  # noqa: F821
    'title': _('CPU Usage'),  # noqa: F821
    'metrics': [('pve_cpu', 'area')],
    'scalars': [
        'pve_cpu:warn',
        'pve_cpu:crit',
    ],
}

graph_info['pve_memory_current'] = {  # noqa: F821
    'title:': _('Memory Usage'),  # noqa: F821
    'metrics': [
        ('pve_memory_current', 'area'),
    ],
    'scalars': [
        'pve_memory_current:warn',
        'pve_memory_current:crit',
    ],
}

graph_info['pve_memory_assigned'] = {  # noqa: F821
    'title:': _('Assigned Memory'),  # noqa: F821
    'metrics': [
        ('pve_memory_assigned', 'area'),
    ],
    'legend_scale': 'GB',
    'legend_precision': 2,
}

