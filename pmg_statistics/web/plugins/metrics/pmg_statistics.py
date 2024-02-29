#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# This file is part of the Proxmox Mail Gateway Statistics for Check_MK
# It defines metrc information used in the plugin.
# Author: Chris Pedro
# Date: 2020-06-25


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

check_metrics['check_mk-pmg_statistics'] = {  # noqa: F821
    'avptime': {'name': 'pmg_avptime', },
    'bounces_in': {'name': 'pmg_bounces_in', },
    'bounces_out': {'name': 'pmg_bounces_out', },
    'bytes_in': {'name': 'pmg_bytes_in', },
    'bytes_out': {'name': 'pmg_bytes_out', },
    'count': {'name': 'pmg_count', },
    'count_in': {'name': 'pmg_count_in', },
    'count_out': {'name': 'pmg_count_out', },
    'glcount': {'name': 'pmg_glcount', },
    'junk_in': {'name': 'pmg_junk_in', },
    'junk_out': {'name': 'pmg_junk_out', },
    'pregreet_rejects': {'name': 'pmg_pregreet_rejects', },
    'rbl_rejects': {'name': 'pmg_rbl_rejects', },
    'spamcount_in': {'name': 'pmg_spamcount_in', },
    'spamcount_out': {'name': 'pmg_spamcount_out', },
    'spfcount': {'name': 'pmg_spfcount', },
    'viruscount_in': {'name': 'pmg_viruscount_in', },
    'viruscount_out': {'name': 'pmg_viruscount_out', },
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

metric_info['pmg_avptime'] = {  # noqa: F821
    'title': _('Average Proccessed Time'),  # noqa: F821
    'unit': 's',
    'color': '32/b',
}

metric_info['pmg_bytes_in'] = {  # noqa: F821
    'title': _('Bytes In'),  # noqa: F821
    'unit': 'bytes',
    'color': '33/a',
}

metric_info['pmg_bytes_out'] = {  # noqa: F821
    'title': _('Bytes Out'),  # noqa: F821
    'unit': 'bytes',
    'color': '33/b',
}

metric_info['pmg_count'] = {  # noqa: F821
    'title': _('Message Count'),  # noqa: F821
    'unit': 'count',
    'color': '41/a',
}

metric_info['pmg_count_in'] = {  # noqa: F821
    'title': _('Messages In'),  # noqa: F821
    'unit': 'count',
    'color': '43/a',
}

metric_info['pmg_count_out'] = {  # noqa: F821
    'title': _('Messages Out'),  # noqa: F821
    'unit': 'count',
    'color': '43/b',
}

metric_info['pmg_pregreet_rejects'] = {  # noqa: F821
    'title': _('Pre-Greet Rejects'),  # noqa: F821
    'unit': 'count',
    'color': '15/a',
}

metric_info['pmg_glcount'] = {  # noqa: F821
    'title': _('Greylist Message Count'),  # noqa: F821
    'unit': 'count',
    'color': '16/a',
}

metric_info['pmg_rbl_rejects'] = {  # noqa: F821
    'title': _('RBL Rejects'),  # noqa: F821
    'unit': 'count',
    'color': '21/a',
}

metric_info['pmg_spfcount'] = {  # noqa: F821
    'title': _('SPF Rejects'),  # noqa: F821
    'unit': 'count',
    'color': '22/a',
}

metric_info['pmg_bounces_in'] = {  # noqa: F821
    'title': _('Bounced Messages In'),  # noqa: F821
    'unit': 'count',
    'color': '12/a',
}

metric_info['pmg_bounces_out'] = {  # noqa: F821
    'title': _('Bounced Messages Out'),  # noqa: F821
    'unit': 'count',
    'color': '12/b',
}

metric_info['pmg_junk_in'] = {  # noqa: F821
    'title': _('Junk Messages In'),  # noqa: F821
    'unit': 'count',
    'color': '13/a',
}

metric_info['pmg_junk_out'] = {  # noqa: F821
    'title': _('Junk Messages Out'),  # noqa: F821
    'unit': 'count',
    'color': '13/b',
}

metric_info['pmg_spamcount_in'] = {  # noqa: F821
    'title': _('Spam Messages In'),  # noqa: F821
    'unit': 'count',
    'color': '14/a',
}

metric_info['pmg_spamcount_out'] = {  # noqa: F821
    'title': _('Spam Messages Out'),  # noqa: F821
    'unit': 'count',
    'color': '14/b',
}

metric_info['pmg_viruscount_in'] = {  # noqa: F821
    'title': _('Virus Messages In'),  # noqa: F821
    'unit': 'count',
    'color': '15/a',
}

metric_info['pmg_viruscount_out'] = {  # noqa: F821
    'title': _('Virus Messages Out'),  # noqa: F821
    'unit': 'count',
    'color': '15/b',
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
    'type': 'linear',
    'segments': ['pmg_avptime'],
    'total': 'pmg_avptime:warn',
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

graph_info['pmg_avptime'] = {  # noqa: F821
    'title': _('Average Mail Proccessed Time'),  # noqa: F821
    'metrics': [('pmg_avptime', 'area')],
    'scalars': [
        'pmg_avptime:warn',
        'pmg_avptime:crit',
    ],
}

graph_info['pmg_bytes'] = {  # noqa: F821
    'title:': _('Total Traffic'),  # noqa: F821
    'metrics': [
        ('pmg_bytes_in', 'area'),
        ('pmg_bytes_out', '-area'),
    ],
}

graph_info['pmg_counts'] = {  # noqa: F821
    'title:': _('Total Message Count'),  # noqa: F821
    'metrics': [
        ('pmg_count_in', 'area'),
        ('pmg_count_out', '-area'),
        ('pmg_count', 'line'),
    ],
}

graph_info['pmg_bounces'] = {  # noqa: F821
    'title': _('Filtering Checks'),  # noqa: F821
    'metrics': [
        ('pmg_bounces_in', 'line'),
        ('pmg_bounces_out', '-line'),
        ('pmg_junk_in', 'line'),
        ('pmg_junk_out', '-line'),
        ('pmg_spamcount_in', 'line'),
        ('pmg_spamcount_out', '-line'),
        ('pmg_viruscount_in', 'line'),
        ('pmg_viruscount_out', '-line'),
    ],
}

graph_info['pmg_prefilter_checks'] = {  # noqa: F821
    'title': _('Pre-Filtering Checks'),  # noqa: F821
    'metrics': [
        ('pmg_pregreet_rejects', 'stack'),
        ('pmg_glcount', 'stack'),
        ('pmg_rbl_rejects', 'stack'),
        ('pmg_spfcount', 'stack'),
    ]
}

