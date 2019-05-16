#!/usr/bin/env python3

import connexion
import atexit
from swagger_server.database import database
import os


from swagger_server import encoder
from flask_cors import CORS


# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

def main():
    global app
    global auth
    database.connect()
    app = connexion.App(__name__, specification_dir='./swagger/', debug=True)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Game of Life backend'})
    # auth = OIDCAuthentication(app=app, provider_configuration_info=provider_config, client_registration_info=client_info)
    CORS(app.app)
    app.run(port=port)

    # @app.route("/foo")
    # @auth.ocid_auth
    # def foo():
    #     return "foo"


if __name__ == '__main__':
    main()

# When shutting down the app server, use ``client.disconnect()`` to properly
# logout and end the ``client`` session
@atexit.register
def shutdown():
    database.disconnect()
# Configure access to App ID service for the OpenID Connect client
