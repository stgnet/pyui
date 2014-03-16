import element as pui


class jumbotron(pui.element):
    def __init__(self, **kwargs):
        pui.element.__init__(self, 'div', **kwargs)
        self.addClass('jumbotron')

# vim:sw=4:ts=4:expandtab:textwidth=79
