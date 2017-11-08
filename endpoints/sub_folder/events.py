#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Define Event Mongo Model through Eve framework.
"""
from datetime import datetime

from evedom import Endpoint

__author__ = "nam4dev"
__created__ = '08/11/2017'


class Events(Endpoint):
    """
    Events Endpoint:

        * name
        * specification
        * specific hooks
    """
    name = "events"
    spec = {
        # by default the standard item entry point is defined as
        # '/event/<ObjectId>/'. We leave it untouched, and we also enable an
        # additional read-only entry point. This way consumers can also perform GET
        # requests at '/event/<title>/'.
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'title'
        },
        'public_methods': [],
        'public_item_methods': [],
        'datasource': {'default_sort': [('start', 1)]},
        # Schema definition, based on Cerberus grammar. Check the Cerberus project
        # (https://github.com/nicolaiarocci/cerberus) for details.
        'schema': {
            'title': {
                'type': 'string',
                'required': True,
            },
            'end': {
                'type': 'datetime',
                'required': False,
            },
            'start': {
                'type': 'datetime',
                'required': True,
            },
            'description': {
                'type': 'string',
                'required': False,
                'default': "",
            }
        }
    }

    def _on_methods(self):
        return [
            ('on_pre_GET_{}'.format(self.name), self._on_pre_get),
        ]

    @staticmethod
    def _on_pre_get(resource, lookup):
        lookup["start"] = {'$gte': datetime.now()}
