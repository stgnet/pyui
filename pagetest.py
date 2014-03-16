#!/usr/bin/env python

import pui

print pui.page('Page Name').background('blue').add(
    pui.bootstrap(),
    pui.heading(1, text="this & that")
).asHtml()

# vim:sw=4:ts=4:expandtab:textwidth=79
