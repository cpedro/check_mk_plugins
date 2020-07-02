#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# This file is part of the Proxmox Virtual Environment for Check_MK
# It defines WATO information used in the plugin.
# Author: Chris Pedro
# Date: 2020-07-01


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


def _parameter_valuespec_pmg_avptime():
    return Dictionary(
        elements=[
            (
                'cpu', Tuple(
                    title=_('VM CPU usage'),
                    elements=[
                        Integer(title=_("Warning at"), unit=_("%"),
                                default_value=80),
                        Integer(title=_("Critical at"), unit=_("%"),
                                default_value=90),
                    ],
                ),
            ),
            (
                'memory', Tuple(
                    title=_('VM Memory usage'),
                    elements=[
                        Integer(title=_("Warning at"), unit=_("%"),
                                default_value=80),
                        Integer(title=_("Critical at"), unit=_("%"),
                                default_value=90),
                    ],
                ),
            ),
        ],
        required_keys=['cpu', 'memory'],
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        check_group_name='pve_qemu',
        group=RulespecGroupCheckParametersApplications,
        is_deprecated=False,
        match_type='dict',
        parameter_valuespec=_parameter_valuespec_pmg_avptime,
        title=lambda: _('Proxmox Virtual Environmnet - QEMU VM status'),
    )
)

