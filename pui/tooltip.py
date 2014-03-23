import element as pui


class well(pui.element):
    def __init__(self, url, text=None, **kwargs):
        pui.element.__init__(self, 'a', **kwargs)
        self.attr(rel='tooltip')
        if text:
            self.attr(title=text)

    def Top(self):
        self.attr(data_placement='top')

    def Bottom(self):
        self.attr(data_placement='bottom')

    def Above(self):
        self.attr(data_placement='top')

    def Below(self):
        self.attr(data_placement='bottom')

    def Left(self):
        self.attr(data_placement='left')

    def Right(self):
        self.attr(data_placement='right')

# vim:sw=4:ts=4:expandtab:textwidth=79
