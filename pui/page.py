import element as pui


class page(pui.element):
    """
        generates doctype, html, head, title, meta, body tags
        also loads bootstrap
    """
    def __init__(self, title='Web Page', meta=[]):
        pui.element.__init__(self)
        self.title = title
        self.meta = meta

    def asHtml(self):
        """
            redefine html output for this page
            special case grabs head and tail lists
            and constructs entire page with doctype
        """
        # get the head/tail before contents duplicated
        page_head = self._get_head()
        page_tail = self._get_tail()

        # create fake body element
        body = pui.element('body')
        body.contents = self.contents
        body.attributes = self.attributes

        # construct page with head and body
        html = pui.element('html').add(
            pui.element('head').add(
                pui.element('title').add(pui.text(self.title)),
            ).addList(self.meta).addList(page_head)
        ).add(
            body
        ).addList(page_tail)

        return '<!DOCTYPE html>' + html.asHtml() + '\n'


# vim:sw=4:ts=4:expandtab:textwidth=79
