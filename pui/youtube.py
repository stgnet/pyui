import element as pui


class youtube(pui.element):
    def __init__(self, url, width=640, height=False):
        if not height:
            height = int(640 * 1.777)
        pui.element.__init__(
            self,
            'iframe',
            width=width,
            height=height,
            src=url,
            frameborder=0,
            allowfullscreen=True)

# vim:sw=4:ts=4:expandtab:textwidth=79
