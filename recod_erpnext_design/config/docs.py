# -*- coding: utf-8 -*-
# Copyright (c) 2021, Monogramm and Contributors
# See license.txt
"""Configuration for docs."""

from __future__ import unicode_literals


source_link = "https://github.com/Monogramm/recod_erpnext_design"
docs_base_url = "https://monogramm.github.io/recod_erpnext_design"
headline = "ERPNext application to provide new sample print formats and overall design for ERPNext."
sub_heading = "Use Recod print formats, website themes, etc..."


def get_context(context):
    """Returns the application documentation context.

     :param context: application documentation context"""
    context.brand_html = "Recod ERPNext Design"
    context.source_link = source_link
    context.docs_base_url = docs_base_url
    context.headline = headline
    context.sub_heading = sub_heading
