#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# This file is part of the Ping Probe Plugin for Check_MK
# It defines metric information used in the plugin.
# Author: Chris Pedro
# Date: 2024-03-12


from cmk.gui.i18n import _
from cmk.gui.plugins.metrics.utils import (
    check_metrics, graph_info, metric_info, perfometer_info)


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

check_metrics['check_mk-ping_probe'] = {
    'ping_probe_loss': {'name': 'ping_probe_loss', },
    'ping_probe_min_rtt': {'name': 'ping_probe_min_rtt', },
    'ping_probe_max_rtt': {'name': 'ping_probe_max_rtt', },
    'ping_probe_avg_rtt': {'name': 'ping_probe_avg_rtt', },
    'ping_probe_min_jitter': {'name': 'ping_probe_min_jitter', },
    'ping_probe_max_jitter': {'name': 'ping_probe_max_jitter', },
    'ping_probe_avg_jitter': {'name': 'ping_probe_avg_jitter', },
    'ping_probe_mos': {'name': 'ping_probe_mos', },
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

metric_info['ping_probe_mos'] = {
    'title': _('MOS Score'),
    'unit': '',
    'color': '22/a',
}

metric_info['ping_probe_loss'] = {
    'title': _('Packet Loss'),
    'unit': '%',
    'color': '14/a',
}

metric_info['ping_probe_min_rtt'] = {
    'title': _('Minimum Latency'),
    'unit': 's',
    'color': '33/a',
}

metric_info['ping_probe_max_rtt'] = {
    'title': _('Maximum Latency'),
    'unit': 's',
    'color': '42/a',
}

metric_info['ping_probe_avg_rtt'] = {
    'title': _('Average Latency'),
    'unit': 's',
    'color': '42/b',
}

metric_info['ping_probe_min_jitter'] = {
    'title': _('Minimum Jitter'),
    'unit': 's',
    'color': '31/b',
}

metric_info['ping_probe_max_jitter'] = {
    'title': _('Maximum Jitter'),
    'unit': 's',
    'color': '32/a',
}

metric_info['ping_probe_avg_jitter'] = {
    'title': _('Average Jitter'),
    'unit': 's',
    'color': '32/b',
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

perfometer_info.append(
    {
        "type": "linear",
        "segments": ["ping_probe_mos"],
        "total": 5.0,
    }
)


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

graph_info['ping_probe_mos'] = {
    'title': _('MOS Score'),
    'metrics': [
        ('ping_probe_mos', 'area'),
    ],
    'scalars': [
        'ping_probe_mos:warn',
        'ping_probe_mos:crit',
    ],
}

graph_info['ping_probe_loss'] = {
    'title': _('Packet Loss'),
    'metrics': [
        ('ping_probe_loss', 'area'),
    ],
    'scalars': [
        'ping_probe_loss:warn',
        'ping_probe_loss:crit',
    ],
}

graph_info['ping_probe_latency'] = {
    'title': _('Packet Latency'),
    'metrics': [
        ('ping_probe_max_rtt', 'area'),
        ('ping_probe_min_rtt', 'line'),
        ('ping_probe_avg_rtt', 'line'),
    ],
    'scalars': [
        'ping_probe_avg_rtt:warn',
        'ping_probe_avg_rtt:crit',
    ],
}

graph_info['ping_probe_jitter'] = {
    'title': _('Packet Jitter'),
    'metrics': [
        ('ping_probe_max_jitter', 'area'),
        ('ping_probe_min_jitter', 'line'),
        ('ping_probe_avg_jitter', 'line'),
    ],
    'scalars': [
        'ping_probe_avg_jitter:warn',
        'ping_probe_avg_jitter:crit',
    ],
}

