import os
from evedom import loader

__author__ = "nam4dev"
__created__ = '08/11/2017'

MONGO_HOST = os.environ.get('MONGO_HOST', '127.0.0.1')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')

# All endpoints are read-only by default
PUBLIC_METHODS = ['GET']
PUBLIC_ITEM_METHODS = ['GET']
# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# set up the desired media endpoint
# MEDIA_BASE_URL = 'https://s3-us-west-2.amazonaws.com'
PAGINATION_LIMIT = 75
PAGINATION_DEFAULT = 25

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = loader.domain(
    root=os.path.dirname(__file__), folder='endpoints'
)



