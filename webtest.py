#!/usr/bin/env python
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
#from twisted.web.error import NoResource
from twisted.web.static import File

import pui

navigation = {
    "Demo": "/",
    "Test": "/test",
}


def page():
    return pui.page("Page Name").add(
        pui.navbar(navigation)
    )


class WebHandler(Resource):
    def __init__(self, name):
        Resource.__init__(self)
        self.name = name

    def render_GET(self, request):
        return pui.page('Pui Demo').add(
            pui.bootstrap(),
            pui.jumbotron().add(
                pui.heading(3, text="python ui demo")
            )
        ).asHtml()


class WebRequest(Resource):
#    isLeaf = True

    def getChild(self, name, request):
#        if name != "test":
#            return NoResource()
        return WebHandler(name)

resource = WebRequest()
#resource.putChild("etc", File("/etc"))
factory = Site(resource)
reactor.listenTCP(8080, factory)
reactor.run()

# vim:sw=4:ts=4:expandtab:textwidth=79
