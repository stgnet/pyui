import element as pui


class well(pui.element):
    def __init__(self, preformatted_text):
        pui.element.__init__(
            self,
            'pre',
            text=preformatted_text
        )

# vim:sw=4:ts=4:expandtab:textwidth=79
