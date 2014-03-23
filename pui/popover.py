import element as pui


class well(pui.element):
    def __init__(self, text):
        pui.element.__init__(
            self,
            'a',
            href='#',
            rel='popover',
            data_content=text
        )
        self.addReadyScript(popover='$(\'a[rel="popover"]\').popover();')

# vim:sw=4:ts=4:expandtab:textwidth=79
