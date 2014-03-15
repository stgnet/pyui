import itertools

doctype = '<!DOCTYPE html>'
dont_self_close = ['script', 'i', 'iframe', 'div', 'title']
indention = '  '

bootstrap_css_url='//netdna.bootstrapcdn.com/bootswatch/3.0.3/united/bootstrap.min.css'
fontawesome_css_url='//netdna.bootstrapcdn.com/font-awesome/4.0.1/css/font-awesome.min.css'
jquery_js_url='//code.jquery.com/jquery-1.10.1.min.js'
bootstrap_js_url='//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js'


class element(object):
    def __init__(self, tag=None, html=None):
        """
            create an element tag with various properties
            used to construct a nested list of elements
            to make up the entire page
        """
        part = tag.partition(' ') if tag else ('', '', '')
        self.tag = part[0]
        self.attributes = {}
        self.styles = {}
        self.classes = []
        # TODO: parse part[2] into attributes
        self.head = list()  # tags that go in <head>
        self.tail = list()  # usually <script>'s at end of page inside body
        self.contents = list()  # sub content to this element, html or object
        self.raw_html = html

    def _get_head(self):
        return self.head + list(itertools.chain(
            item._get_head() for item in self.contents
            if isinstance(item, element)))

    def _get_tail(self):
        return self.head + list(itertools.chain(
            item._get_tail() for item in self.contents
            if isinstance(item, element)))

    def _get_attr_str(self):
        attrib = ''
        if self.styles:
            self.attributes['style'] = ';'.join(
                key + ': '+self.styles[key] for key in self.styles)
        if self.classes:
            self.attributes['class'] = ' '.join(
                key for key in self.classes)
        for key in self.attributes:
            if self.attributes[key] in [False, None]:
                continue
            if self.attributes[key] is True:
                attrib += ' ' + key
                continue
            attrib += ' ' + key + '="%s"' % self.attributes[key]
        return attrib

    def asHtml(self, level=0):
        """
            recursively walk element tree and generate
            html document, creating tags along the way
        """
        content = self.raw_html if self.raw_html else ''
        content += ''.join(item.asHtml(level + 1) for item in self.contents)
        indent = indention * level
        tag_attr = self.tag + self._get_attr_str()
        if not self.tag:
            html = [content]
        elif content == '' and self.tag not in dont_self_close:
            html = ['\n', indent, '<', tag_attr, ' />']
        elif len(indent) + len(tag_attr) + len(content) < 70:
            html = ['\n', indent, '<', tag_attr, '>', content,
                    '<', self.tag, '/>' ]
        else:
            html = ['\n', indent, '<', tag_attr, '>',
                    content,
                    '\n', indent, '<', self.tag, '/>']
        return ''.join(html)

    def addList(self, things):
        for thing in things:
            if thing:
                if not isinstance(thing, element):
                    thing = element(None, "%s" % thing)
                self.contents.append(thing)
        return self

    def add(self, *things):
        return self.addList(things)

    def attr(self, **kwargs):
        for key in kwargs:
            self.attributes[key] = kwargs[key]
        return self

    def style(self, **kwargs):
        for key in kwargs:
            name = key.replace('_', '-')
            self.styles[name] = kwargs[key]
        return self

    def addClass(self, *args):
        for name in args:
            if name not in self.classes:
                self.classes.append(name)
        return self

    def center(self):
        self.addClass('pagination-centered')
        return self

    def right(self):
        self.addClass('pull-right')
        return self

    def left(self):
        self.addClass('pull-left')
        return self

    def border(self, width=1, color='#888', style='solid'):
        self.style(border=width + 'px ' + style + color)
        return self

    def margin(self, value):
        self.style(margin=value)
        return self

    def marginBottom(self, value):
        self.style(margin_bottom=value)
        return self

    def marginLeft(self, value):
        self.style(margin_left=value)
        return self

    def marginRight(self, value):
        self.style(margin_right=value)
        return self

    def marginTop(self, value):
        self.style(margin_top=value)
        return self

    def background(self, color):
        self.style(background=color)
        return self


class page(element):
    """
        generates doctype, html, head, title, meta, body tags
        also loads bootstrap
    """
    def __init__(self, title='Web Page', meta=[]):
        element.__init__(self)
        self.title = title
        self.meta = meta
        self.head = [
            element('link').attr(
                rel='stylesheet',
                href=bootstrap_css_url,
                type='text/css'
            ),
            element('link').attr(
                rel='stylesheet',
                href=fontawesome_css_url,
                type='text/css'
            ),
        ]
        self.tail = [
            element('script').attr(
                src=jquery_js_url,
                type='text/css'
            ),
            element('script').attr(
                src=bootstrap_js_url,
                type='text/css'
            ),
        ]

    def asHtml(self):
        """
            redefine html output for this page
            special case grabs head and tail lists
            and constructs entire page with doctype
        """
        body = element('body')
        body.contents = self.contents
        body.attributes = self.attributes

        # construct page with head and body
        html = element('html').add(
            element('head').add(
                element('title').add(self.title),
            ).addList(self.meta).addList(self._get_head())
        ).add(
            body
        ).addList(self._get_tail())

        return doctype + html.asHtml()


# vim:sw=4:ts=4:expandtab:textwidth=79
