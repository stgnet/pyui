import element as pui


class link(pui.element):
    def __init__(self, href, **kwargs):
        pui.element.__init__(self, 'a', **kwargs)
        self.attr(href=href)

# vim:sw=4:ts=4:expandtab:textwidth=79
