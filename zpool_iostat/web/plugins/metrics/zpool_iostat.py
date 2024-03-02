#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# This file is part of the ZFS zpool iostat for Check_MK
# It defines metric information used in the plugin.
# Author: Chris Pedro
# Date: 2024-02-27


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

check_metrics['check_mk-zpool_iostat'] = {  # noqa: F821
    'zpool_read_iops': {'name': 'zpool_read_iops', },
    'zpool_write_iops': {'name': 'zpool_write_iops', },
    'zpool_read_wait': {'name': 'zpool_read_wait', },
    'zpool_write_wait': {'name': 'zpool_write_wait', },
    'zpool_read_bw': {'name': 'zpool_read_bw', },
    'zpool_write_bw': {'name': 'zpool_write_bw', },
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

metric_info['zpool_read_iops'] = {  # noqa: F821
    'title': _('Read IOPS'),  # noqa: F821
    'unit': '1/s',
    'color': '11/a',
}

metric_info['zpool_write_iops'] = {  # noqa: F821
    'title': _('Write IOPS'),  # noqa: F821
    'unit': '1/s',
    'color': '13/a',
}

metric_info['zpool_read_wait'] = {  # noqa: F821
    'title': _('Read Latency'),  # noqa: F821
    'unit': 's',
    'color': '31/a',
}

metric_info['zpool_write_wait'] = {  # noqa: F821
    'title': _('Write Latency'),  # noqa: F821
    'unit': 's',
    'color': '33/a',
}

metric_info['zpool_read_bw'] = {  # noqa: F821
    'title': _('Read Bandwidth'),  # noqa: F821
    'unit': 'bytes/s',
    'color': '#00e060',
}

metric_info['zpool_write_bw'] = {  # noqa: F821
    'title': _('Write Bandwidth'),  # noqa: F821
    'unit': 'bytes/s',
    'color': '#0080e0',
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
    "type": "dual",
    "perfometers": [
        {
            "type": "logarithmic",
            "metric": "zpool_read_wait",
            "half_value": 0.01,
            "exponent": 10.0,
        },
        {
            "type": "logarithmic",
            "metric": "zpool_write_wait",
            "half_value": 0.01,
            "exponent": 10.0,
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

graph_info['zpool_iops'] = {  # noqa: F821
    'title': _('IOPS'),  # noqa: F821
    'metrics': [
        ('zpool_read_iops', 'area'),
        ('zpool_write_iops', '-area'),
    ],
}

graph_info['zpool_latency'] = {  # noqa: F821
    'title': _('Latency'),  # noqa: F821
    'metrics': [
        ('zpool_read_wait', 'area'),
        ('zpool_write_wait', '-area'),
    ],
    'scalars': [
        ('zpool_read_wait:warn', _('Warning (Read)')),  # noqa: F821
        ('zpool_read_wait:crit', _('Critical (Read)')),  # noqa: F821
        ('zpool_write_wait:warn', _('Warning (Write)')),  # noqa: F821
        ('zpool_write_wait:crit', _('Critical (Write)')),  # noqa: F821
    ],
}

graph_info['zpool_bw'] = {  # noqa: F821
    'title': _('Bandwidth'),  # noqa: F821
    'metrics': [
        ('zpool_read_bw', 'area'),
        ('zpool_write_bw', '-area'),
    ],
}

