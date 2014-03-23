#!/usr/bin/env python

import pui

# python doesn't retain order in a dict,
# so use a list of links instead
navigation = [
    pui.link('/', text="Demo"),
    pui.link('/test', text="Test ").add(pui.icon('star')),
    pui.link('/form', text="Form"),
    pui.dropdown(text="Drop ^").menu(
        pui.link('/drop1', text="First"),
        pui.link('/drop2', text="Second"),
    )
]


def page(*content):
    return pui.page("Python User Interface").add(
        pui.bootstrap('cerulean'),
        pui.navbar(navigation).add(
            pui.link('/', _class='navbar-brand', text='PUI')
        )
    ).addList(content).asHtml()


print page(pui.paragraph(text="test"))

# vim:sw=4:ts=4:expandtab:textwidth=79
