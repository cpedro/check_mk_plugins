#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# This file is part of the Proxmox Mail Gateway Statistics for Check_MK
# It defines metrc information used in the plugin.
# Author: Chris Pedro
# Date: 2020-06-29


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
                'avptime',
                Tuple(
                    title=_('Average mail process time (in seconds).'),
                    elements=[
                        Integer(title=_("Warning at"), unit=_("secs"),
                                default_value=10),
                        Integer(title=_("Critical at"), unit=_("secs"),
                                default_value=20),
                    ],
                ),
            ),
        ],
        required_keys=['avptime'],
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        check_group_name='pmg_statistics',
        group=RulespecGroupCheckParametersApplications,
        is_deprecated=False,
        match_type='dict',
        parameter_valuespec=_parameter_valuespec_pmg_avptime,
        title=lambda: _('Proxmox Mail Gateway Avg. Mail Process Time'),
    )
)

