#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
WSGI script

Setup Application, Authentication, ...

"""
import os

from eve import Eve

from evedom import loader
# from your_app.authentication.token import TokenBasedAuth

__author__ = "nam4dev"
__created__ = '08/11/2017'


ROOT_PATH = os.path.dirname(
        os.path.abspath(__file__)
    )
EVE_SETTINGS = os.path.join(ROOT_PATH, 'settings.py')


def runner(*_, **options):
    """
    A simple runner

    Args:
        *_:
        **options:

    Returns:
        Flask App run
    """
    arguments = dict(
        debug=1,
        port=5000,
    )
    arguments.update(options)

    if 'EVE_SETTINGS' not in os.environ:
        os.environ['EVE_SETTINGS'] = EVE_SETTINGS

    application = Eve(
        settings=EVE_SETTINGS,
        # auth=TokenBasedAuth,
    )
    application.root_path = ROOT_PATH

    with application.app_context():
        loader.init()

    return application.run(**arguments)


if __name__ == "__main__":
    exit(runner())

