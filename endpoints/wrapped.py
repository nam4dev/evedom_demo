#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
My super cool wrapped service
"""
from evedom import Endpoint

from flask import current_app

__author__ = "nam4dev"
__created__ = '08/11/2017'


class WrappedService(Endpoint):
    """
    Endpoint to a Custom service
    """
    name = 'service'
    wrapper = True

    def _register(self):
        """
        Allow to register any custom endpoint
        """
        current_app.route(
            '/wrapped/service/', methods=['GET']
        )(self._serve)

    def _serve(self):
        items = []

        # Process your service here...

        return self.dumps({
            'items': items,
            'count': len(items),
        }, indent=4)
