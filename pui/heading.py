import element as pui


class heading(pui.element):
    def __init__(self, level, **kwargs):
        pui.element.__init__(self, "h%d" % level, **kwargs)

# vim:sw=4:ts=4:expandtab:textwidth=79
