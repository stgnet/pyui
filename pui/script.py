import element as pui


class well(pui.element):
    def __init__(self, code):
        pui.element.__init__(
            self,
            'script',
            type='text/javascript',
            html=code
        )

# vim:sw=4:ts=4:expandtab:textwidth=79
