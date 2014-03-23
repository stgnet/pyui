import cgi

dont_self_close = ['script', 'i', 'iframe', 'div', 'title']
indention = '  '
#always_break_before = ['ul', 'li', 'script', 'meta']
always_break_before = []


class element(object):
    def html_entities(self, string):
        return cgi.escape(string)

    def __init__(self, tag=None, **kwargs):
        """
            create an element tag with various properties
            used to construct a nested list of elements
            to make up the entire page
        """
        self.tag = tag if tag else ''  # "%s" % id(self)
        self.attributes = {}
        self.styles = {}
        self.classes = []
        self.head = list()  # tags that go in <head>
        self.tail = list()  # usually <script>'s at end of page inside body
        self.ready = dict()  # document ready scripts (named for collision)
        self.contents = list()  # sub content to this element (nested)
        self.navmenu = list()   # nested navigation menus
        self.raw_html = ''      # html inside this tag

        for key in kwargs:
            if not kwargs[key]:
                continue
            elif key is 'html':
                self.raw_html += kwargs[key]
            elif key is 'text':
                self.raw_html += self.html_entities(kwargs[key])
            elif key is '_class':
                self.classes = kwargs[key].split(' ')
            else:
                self.attr(**{key: kwargs[key]})

    def get_id(self):
        if ('id' not in self.attributes):
            self.attributes['id'] = "id%s" % id(self)
        return self.attributes['id']

    def _get_head(self):
        head = self.head
        for subelement in self.contents:
            for item in subelement._get_head():
                head.append(item)
        return head

    def _get_tail(self):
        tail = self.tail
        for subelement in self.contents:
            for item in subelement._get_tail():
                tail.append(item)
        return tail

    def _get_ready(self):
        ready = self.ready
        for subelement in self.contents:
            for name, script in subelement._get_ready().iteritems():
                ready[name] = script
        # also walk the navmenu
        for subelement in self.navmenu:
            for name, script in subelement._get_ready().iteritems():
                ready[name] = script
        return ready

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
        indent = indention * level
        content = self.raw_html if self.raw_html else ''
        length = len(content)
        #content += ''.join(item.asHtml(level + 1) for item in self.contents)
        for item in self.contents:
            html = item.asHtml(level + 1)
            if not html.startswith('\n') and html.startswith('<'):
                if length + len(html) > 70:
                    html = '\n' + indent + indention + html
                    length = 0
            content += html
            length += len(html)

        if not self.tag:
            return content
        tag_attr = self.tag + self._get_attr_str()

        if not content and self.tag not in dont_self_close:
            return ''.join(['<', tag_attr, ' />'])

        if content.startswith('\n'):
            return ''.join(['\n', indent, '<', tag_attr, '>',
                            content,
                            '\n', indent, '</', self.tag, '>'])

        if len(content) + len(indent) > 70:
            return ''.join(['\n', indent, '<', tag_attr, '>',
                            '\n', indent, indention, content,
                            '\n', indent, '</', self.tag, '>'])

        if self.tag in always_break_before:
            return ''.join(['\n', indent, '<', tag_attr, '>',
                            content,
                            '</', self.tag, '>'])

        return ''.join(['<', tag_attr, '>',
                        content,
                        '</', self.tag, '>'])

    def addList(self, things):
        for thing in things:
            if thing:
                if not isinstance(thing, element):
                    # ad as separate object to retain in supplied order
                    thing = element(None, html="%s" % thing)
                self.contents.append(thing)
        return self

    def add(self, *things):
        return self.addList(things)

    def menu(self, *things):
        for thing in things:
            self.navmenu.append(thing)
        return self

    def attr(self, **kwargs):
        for key in kwargs:
            if key is '_class':
                raise 'not handled'
            name = key.replace('_', '-')
            self.attributes[name] = kwargs[key]
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

    def addReadyScript(self, **kwargs):
        for key in kwargs:
            self.ready[key] = kwargs[key]

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

# vim:sw=4:ts=4:expandtab:textwidth=79
