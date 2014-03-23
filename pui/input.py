import element as pui


class input(pui.element):
    def __init__(self, name, **kwargs):
        pui.element.__init__(self, 'input', **kwargs)
        self.attr(name=name)

# vim:sw=4:ts=4:expandtab:textwidth=79
