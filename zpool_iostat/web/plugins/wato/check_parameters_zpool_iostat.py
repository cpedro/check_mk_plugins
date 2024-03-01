#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# This file is part of the ZFS zpool iostat for Check_MK
# It defines WATO information used in the plugin.
# Author: Chris Pedro
# Date: 2024-02-27


from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Integer,
    Tuple,
)
from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithoutItem,
    rulespec_registry,
    RulespecGroupCheckParametersStorage,
)


def _parameter_valuespec_zpool_iostat():
    return Dictionary(
        elements=[
            (
                'zpool_read_wait', Tuple(
                    title=_('Read latency'),
                    elements=[
                        Integer(title=_("Warning at"), unit=_("ms"),
                                default_value=10),
                        Integer(title=_("Critical at"), unit=_("ms"),
                                default_value=50),
                    ],
                ),
            ),
            (
                'zpool_write_wait', Tuple(
                    title=_('Write latency'),
                    elements=[
                        Integer(title=_("Warning at"), unit=_("ms"),
                                default_value=10),
                        Integer(title=_("Critical at"), unit=_("ms"),
                                default_value=50),
                    ],
                ),
            ),
        ],
        required_keys=['zpool_read_wait', 'zpool_write_wait'],
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        check_group_name='zpool_iostat',
        group=RulespecGroupCheckParametersStorage,
        is_deprecated=False,
        match_type='dict',
        parameter_valuespec=_parameter_valuespec_zpool_iostat,
        title=lambda: _('ZFS pool iostat'),
    )
)

