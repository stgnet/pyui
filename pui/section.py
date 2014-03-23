import element as pui


class well(pui.element):
    def __init__(self, url, **kwargs):
        pui.element.__init__(self, 'section', **kwargs)

# vim:sw=4:ts=4:expandtab:textwidth=79
