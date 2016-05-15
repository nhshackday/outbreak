"""
outbreak - Our OPAL Application
"""
from opal.core import application

class Application(application.OpalApplication):
    schema_module = 'outbreak.schema'
    flow_module   = 'outbreak.flow'
    javascripts   = [
        'js/outbreak/routes.js',
        'js/outbreak/flow.js',
        'js/outbreak/controllers/outbreak_add_episode.js',
        'js/opal/controllers/discharge.js',

    ]
    styles = [
        'css/outbreak.css'
    ]
