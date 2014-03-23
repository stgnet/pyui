import element as pui


class caret(pui.element):
    def __init__(self, **kwargs):
        pui.element.__init__(self, 'span', **kwargs)
        self.addClass('caret')

# vim:sw=4:ts=4:expandtab:textwidth=79
