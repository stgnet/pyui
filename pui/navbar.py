import element as pui
import div


class navbar(pui.element):
    """
        generates doctype, html, head, title, meta, body tags
        also loads bootstrap
    """
    def __init__(self, navigation):
        pui.element.__init__(self, 'x-navbar')
        self.navmenu = navigation

    def _nav_list(self, elements, dropdown=False):
        ul = pui.element('ul')

        if dropdown:
            ul.addClass('dropdown-menu')
            dropdown_id = dropdown.get_id()
            ul.attr(role="menu", aria_labelledby=dropdown_id)
        else:
            ul.addClass('nav', 'navbar-nav')

        for item in elements:
            li = pui.element('li')
            li.add(item)
            if item.navmenu:
                if 'dropdown' in str(type(item)):
                    li.add(self._nav_list(item.navmenu, item))
                    li.addClass('dropdown')
                else:
                    li.add(self._nav_list(item.navmenu))

            ul.add(li)
        return ul

    def asHtml(self, level):
        """
            redefine html output for this object
            contents are put in header (usually brand)
            navigation table used to generate navlist
        """
        div_navbar_main = div.div('navbar-collapse collapse')
        div_navbar_main.add(self._nav_list(self.navmenu))

        div_navbar = div.div('navbar navbar-default').add(
            div.div('navbar-header').addList(self.contents).add(
                # mobile navbar ugliness
                pui.element(
                    'button',
                    _class='navbar-toggle',
                    type='button',
                    data_toggle='collapse',
                    data_target='.navbar-main'
                ).add(
                    pui.element('span', _class='icon-bar'),
                    pui.element('span', _class='icon-bar'),
                    pui.element('span', _class='icon-bar'),
                )
            ),
            div_navbar_main
        )

        return div_navbar.asHtml(level)

# vim:sw=4:ts=4:expandtab:textwidth=79
