# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt
"""Configuration for desktop."""

from __future__ import unicode_literals

from frappe import _


def get_data():
    """Returns the application desktop icons configuration."""
    return [
        {
            "module_name": "Recod ERPNext Design",
            "color": "grey",
            "icon": "octicon octicon-paintcan",
            "type": "module",
            "label": _("Recod ERPNext Design")
        }
    ]
