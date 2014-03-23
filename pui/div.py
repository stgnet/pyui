import element as pui


class div(pui.element):
    def __init__(self, initial_class, **kwargs):
        pui.element.__init__(self, 'div', **kwargs)
        self.addClass(initial_class)

# vim:sw=4:ts=4:expandtab:textwidth=79
