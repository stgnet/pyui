import element as pui


class well(pui.element):
    def __init__(self, url, **kwargs):
        pui.element.__init__(self, 'div', **kwargs).addClass('well')

# vim:sw=4:ts=4:expandtab:textwidth=79
