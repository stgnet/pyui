import element as pui


class icon(pui.element):
    def __init__(self, icon, **kwargs):
        pui.element.__init__(self, 'span', **kwargs)
        if icon[0:10] != 'glyphicon-':
            icon = 'glyphicon-' + icon
        self.addClass('glyphicon')
        self.addClass(icon)

# vim:sw=4:ts=4:expandtab:textwidth=79
