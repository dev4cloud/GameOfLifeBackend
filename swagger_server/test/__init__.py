import logging

import connexion
from flask_testing import TestCase

from swagger_server.encoder import JSONEncoder
from swagger_server.database import database


class DataBaseMock():

    def create_document(self, document):
        logging.info(document)

class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        database.set_database(DataBaseMock())
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        return app.app
