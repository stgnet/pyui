import element as pui


class bootstrap(pui.element):
    def __init__(self, theme=None):
        """
            load bootstrap (requires use of page object)
            see http://bootswatch.com and http://bootstrapcdn.com for themes
        """
        pui.element.__init__(self)

        bootstrap_cdn = '//netdna.bootstrapcdn.com'
        bootstrap_version = '3.1.1'
        bootstrap_css = 'bootstrap.min.css'
        bootstrap_js = 'bootstrap.min.js'

        bootstrap_css_url = '/'.join([
            bootstrap_cdn,
            'bootswatch' if theme else 'bootstrap',
            bootstrap_version,
            theme if theme else 'css',
            bootstrap_css
        ])

        bootstrap_js_url = '/'.join([
            bootstrap_cdn,
            'bootstrap',
            bootstrap_version,
            'js',
            bootstrap_js
        ])

        jquery_js_url = '//code.jquery.com/jquery-1.10.1.min.js'

        self.head.append(
            pui.element(
                'link',
                rel='stylesheet',
                href=bootstrap_css_url,
                type='text/css'
            )
        )

        # mobile viewport meta
        self.head.append(
            pui.element(
                'meta',
                name="viewport",
                content="width=device-width, initial-scale=1"
            )
        )

        self.tail.append(
            pui.element(
                'script',
                src=jquery_js_url,
            )
        )

        self.tail.append(
            pui.element(
                'script',
                src=bootstrap_js_url,
            )
        )

# vim:sw=4:ts=4:expandtab:textwidth=79
