"""
outbreak - Our OPAL Application
"""
from opal.core import application

class Application(application.OpalApplication):
    schema_module = 'outbreak.schema'
    flow_module   = 'outbreak.flow'
    javascripts   = [
        'js/outbreak/routes.js',
        'js/opal/controllers/discharge.js'
    ]