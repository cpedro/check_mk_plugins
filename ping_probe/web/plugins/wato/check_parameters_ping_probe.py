#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# This file is part of the Ping Probe Plugin for Check_MK
# It defines WATO information used in the plugin.
# Author: Chris Pedro
# Date: 2024-03-12


from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Integer,
    Tuple,
)
from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithoutItem,
    rulespec_registry,
    RulespecGroupCheckParametersNetworking,
)


def _parameter_valuespec_ping_probe():
    return Dictionary(
        elements=[
            (
                'ping_probe_loss', Tuple(
                    title=_('Packet Loss'),
                    elements=[
                        Integer(title=_("Warning at"), unit=_("%"),
                                default_value=10),
                        Integer(title=_("Critical at"), unit=_("%"),
                                default_value=20),
                    ],
                ),
            ),
            (
                'ping_probe_avg_rtt', Tuple(
                    title=_('Average Latency'),
                    elements=[
                        Integer(title=_("Warning at"), unit=_("ms"),
                                default_value=75),
                        Integer(title=_("Critical at"), unit=_("ms"),
                                default_value=100),
                    ],
                ),
            ),
            (
                'ping_probe_avg_jitter', Tuple(
                    title=_('Average Jitter'),
                    elements=[
                        Integer(title=_("Warning at"), unit=_("ms"),
                                default_value=20),
                        Integer(title=_("Critical at"), unit=_("ms"),
                                default_value=30),
                    ],
                ),
            ),
            (
                'ping_probe_mos', Tuple(
                    title=_('MOS Score'),
                    elements=[
                        Integer(title=_("Warning at"), unit=_(""),
                                default_value=4),
                        Integer(title=_("Critical at"), unit=_(""),
                                default_value=3),
                    ],
                ),
            ),
        ],
        required_keys=[
            'ping_probe_loss',
            'ping_probe_avg_rtt',
            'ping_probe_avg_jitter',
            'ping_probe_mos',
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        check_group_name='ping_probe',
        group=RulespecGroupCheckParametersNetworking,
        is_deprecated=False,
        match_type='dict',
        parameter_valuespec=_parameter_valuespec_ping_probe,
        title=lambda: _('Networking Ping Probe'),
    )
)

