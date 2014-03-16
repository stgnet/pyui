#!/usr/bin/env python

import pui

print pui.page('Page Name').background('blue').add(
    pui.bootstrap(),
    pui.element('H1')
).asHtml()

# vim:sw=4:ts=4:expandtab:textwidth=79
