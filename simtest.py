#!/usr/bin/env python

import pui

print pui.element('one').add(
    pui.element('two').attr(alpha='123', beta=True)
).html()

# vim:sw=4:ts=4:expandtab:textwidth=79
