import element as pui


class paragraph(pui.element):
    def __init__(self, text=None):
        pui.element.__init__(self, 'p', text=text)

# vim:sw=4:ts=4:expandtab:textwidth=79
