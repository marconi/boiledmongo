from pymongo import Connection
from pymongo.errors import ConnectionFailure

from pyramid.config import Configurator
from pyramid.events import NewRequest, subscriber
from boiledmongo.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)

    config.add_static_view('static', 'boiledmongo:static')

    # connect to mongodb
    try:
        connection = Connection(host=settings['mongodb.host'],
                                port=int(settings['mongodb.port']))
        db_connection = connection[settings['mongodb.db']]
        config.registry.settings['db_connection'] = db_connection
    except ConnectionFailure:
        raise Exception('Unable to connect to MongoDB')

    # includes
    config.include('boiledmongo.views.add_routes')

    config.scan(package='boiledmongo.lib')
    config.scan(package='boiledmongo.views')
    return config.make_wsgi_app()


@subscriber(NewRequest)
def add_mongo_db(event):
    settings = event.request.registry.settings
    event.request.db = settings['db_connection']
