import itertools

doctype = '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">'
dont_close = ['script', 'i', 'iframe', 'div', 'title']


class element(object):
    def __init__(self, tag):
        """
            create an element tag with various properties
            used to construct a nested list of elements
            to make up the entire page

            tag can be 'xyz' or 'xyz var="value"'
        """
        part = tag.partition(' ')
        self.tag = part[0]
        self.attributes = {}
        # TODO: parse part[2] into attributes
        self.head = list()  # tags that go in <head>
        self.tail = list()  # usually <script>'s at end of page inside body
        self.contents = list()  # sub content to this element, html or object

    def _get_head(self):
        return self.head + itertools.chain(
            x._get_head() for x in self.html if isinstance(x, element))

    def html(self):
        attrib = ''.join(' ' + k + '="' + self.attributes[k] + '"'
                         for k in self.attributes)
        content = ''.join(item.html() for item in self.contents)
        if content == '' and self.tag not in dont_close:
            return '<' + self.tag + attrib + ' />\n'
        return ''.join(
            '<', self.tag, attrib, '>',
            content,
            '<', self.tag, '/>\n')

    def add(self, *things):
        for thing in things:
            self.contents.append(thing)
        return self

    def addList(self, things):
        for thing in things:
            self.html.append(thing)
        return self

    def attr(self, **kwargs):
        for key in kwargs:
            self.attributes[key] = kwargs[key]
        return self


class page(element):
    """
        generates doctype, html, head, title, meta, body tags
        also loads bootstrap
    """
    def __init(self, title='', meta=None):
        # generating html, but containing body tag
        element.__init__(self, 'body')
        self.title = title
        self.meta = None

    def html(self):
        """
            redefine html output for this page
            special case grabs head and tail lists
            and constructs entire page with doctype
        """
        head = element('head').add(
            element('title').add(self.Title)
        ).addList(self.meta).addList(self._get_head())

        html_tag = element('html').add(head, self).addList(self._get_tail())

        return doctype + html_tag.html()


# vim:sw=4:ts=4:expandtab:textwidth=79
