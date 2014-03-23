import element as pui


class page(pui.element):
    """
        generates doctype, html, head, title, meta, body tags
        also loads bootstrap
    """
    def __init__(self, title='Web Page', **kwargs):
        pui.element.__init__(self, 'page', **kwargs)
        self.title = title
        self.head.append(
            pui.element(
                'meta',
                charset='utf-8'
            )
        )

    def asHtml(self):
        """
            redefine html output for this page
            special case grabs head and tail lists
            and constructs entire page with doctype
        """
        # get the head/tail before contents duplicated
        page_head = self._get_head()
        page_tail = self._get_tail()
        page_ready = self._get_ready()

        # construct ready script section
        ready_script = None
        if page_ready:
            scripts = '\n'.join(page_ready.itervalues())
            ready_script_func = '\n'.join([
                "$(document).ready(function(){",
                scripts,
                "});"
            ])
            ready_script = pui.element(
                'script',
                type='text/javascript',
                html=ready_script_func)

        # create fake body element
        body = pui.element('body')
        body.contents = self.contents
        body.attributes = self.attributes

        # construct page with head and body
        html = pui.element('html').add(
            pui.element('head').add(
                pui.element('title', text=self.title),
            ).addList(page_head)
        ).add(
            body.addList(page_tail).add(ready_script)
        )

        return '<!DOCTYPE html>' + html.asHtml() + '\n'


# vim:sw=4:ts=4:expandtab:textwidth=79
