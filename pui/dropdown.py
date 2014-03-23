import element as pui


class dropdown(pui.element):
    def __init__(self, **kwargs):
        pui.element.__init__(self, 'a', **kwargs)
        self.attr(href='#', data_toggle='dropdown', role='button',
                  data_target='#')
        self.addClass('dropdown-toggle')
        self.addReadyScript(
            dropdown="$('.dropdown-toggle').dropdown();")

# vim:sw=4:ts=4:expandtab:textwidth=79
