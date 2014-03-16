######################################################################
# PUI - Python User Interface
# Copyright (c) 2014 Scott Griepentrog
# MIT License
#
# Dynamic functional web page creation
#
# Example:
#
# print pui.page('My Page Title').add(
#           pui.heading(1,"Page Heading"),
#           pui.paragraph("This isn't very hard!"),
#       ).asHtml()
#
######################################################################

import os
import sys
import glob
import imp

import element


class puiBorg:
    def __init__(self):
        """
            find *.py, load them
            add their uniqueness to our own

            Allows complicated set of classes
            to appear as part of one single module,
            but much easier to manage code when
            broken out into individual files
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.append(script_dir)
        for pyfile in glob.glob(script_dir + '/*.py'):
            pyclass = os.path.splitext(os.path.basename(pyfile))[0]
            if pyclass.startswith('_'):
                continue
            # find and load the module
            # http://docs.python.org/2/library/imp.html
            if pyclass not in sys.modules:
                fp, pathname, description = imp.find_module(
                    pyclass, [script_dir])
                imp.load_module(pyclass, fp, pathname, description)
                if fp:
                    fp.close()

            for attr, val in sys.modules[pyclass].__dict__.iteritems():
                if not attr.startswith('_') and callable(val):
                    self.__dict__[attr] = sys.modules[pyclass].__dict__[attr]

    def __call__(self):
        """
            do something?
        """
        element

sys.modules[__name__] = puiBorg()

# vim:sw=4:ts=4:expandtab:textwidth=79
