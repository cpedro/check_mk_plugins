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
    RulespecGroupCheckParametersApplications,
)


def _parameter_valuespec_zpool_iostat():
    return Dictionary(
        elements=[
            (
                'read_wait', Tuple(
                    title=_('ZFS pool read latency'),
                    elements=[
                        Integer(title=_("Warning at"), unit=_("s"),
                                default_value=0.01),
                        Integer(title=_("Critical at"), unit=_("s"),
                                default_value=0.05),
                    ],
                ),
            ),
            (
                'write_wait', Tuple(
                    title=_('ZFS pool write latency'),
                    elements=[
                        Integer(title=_("Warning at"), unit=_("s"),
                                default_value=0.01),
                        Integer(title=_("Critical at"), unit=_("s"),
                                default_value=0.05),
                    ],
                ),
            ),
        ],
        required_keys=['read_wait', 'write_wait'],
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        check_group_name='zpool_iostat',
        group=RulespecGroupCheckParametersApplications,
        is_deprecated=False,
        match_type='dict',
        parameter_valuespec=_parameter_valuespec_zpool_iostat,
        title=lambda: _('ZFS pool status'),
    )
)

