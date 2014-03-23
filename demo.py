#!/usr/bin/env python
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
#from twisted.web.error import NoResource
#from twisted.web.static import File

import pui

# python doesn't retain order in a dict,
# so use a list of links instead
navigation = [
    pui.link('/', text="Demo"),
    pui.link('/test', text="Test ").add(pui.icon('star')),
    pui.link('/form', text="Form"),
    pui.dropdown(text="Drop ^").menu(
        pui.link('/drop1', text="First"),
        pui.link('/drop2', text="Second"),
    )
]


def page(*content):
    return pui.page("Python User Interface").add(
        pui.bootstrap('cerulean'),
        pui.navbar(navigation).add(
            pui.link('/', _class='navbar-brand', text='PUI')
        )
    ).addList(content).asHtml()


def homePage():
    return page(
        pui.jumbotron().add(
            pui.heading(1, text="Python User Interface Demo"),
            pui.paragraph().add(
                "test&nbsp;html"
            )
        )
    )


def formPage():
    login = [
        pui.input('username', type="text", desc="Email"),
        pui.input('password', type="password", desc="Password"),
        pui.input('remember', type="checkbox", desc="Remember Me"),
        pui.input('submit', type="button", value="Sign In"),
    ]

    target = pui.div(text="Post data will appear here")

    return page(
        pui.div().add(
            pui.form(login)
        ),
        pui.well().add(
            target
        )
    )


def noPage(name):
    message = "Page /%s not found" % name
    return page(
        pui.jumbotron().add(
            pui.heading(3, text=message),
            pui.paragraph(text="That a 404 error!")
        )
    )


class WebRequest(Resource):
    def getChild(self, name, request):
        self.name = name
        return self

    def render_GET(self, request):
        if not self.name:
            return homePage()

        if self.name is 'form':
            return formPage()

        return noPage(self.name)

resource = WebRequest()
#resource.putChild("etc", File("/etc"))
#resource.putChild("/", Home())
factory = Site(resource)
reactor.listenTCP(8080, factory)
reactor.run()

# vim:sw=4:ts=4:expandtab:textwidth=79
