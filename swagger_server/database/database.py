import json
import os

client = None
database = None


def connect():
    global client
    global database
    from cloudant.client import Cloudant
    db_name = 'gol_data'

    if 'VCAP_SERVICES' in os.environ:
        vcap = json.loads(os.getenv('VCAP_SERVICES'))
        print('Found VCAP_SERVICES')
        if 'cloudantNoSQLDB' in vcap:
            creds = vcap['cloudantNoSQLDB'][0]['credentials']
            user = creds['username']
            apikey = creds['apikey']
            iam_apikey_name = creds['iam_apikey_name']
            url = 'https://' + creds['host']
            #client = Cloudant(cloudant_user=user, auth_token=password, url=url, connect=True, auto_renew=True)
            client = Cloudant.iam(account_name=user, iam_apikey_name=iam_apikey_name, api_key=apikey, connect=True)
            database = client.create_database(db_name)
    elif "CLOUDANT_URL" in os.environ:
        client = Cloudant(os.environ['CLOUDANT_USERNAME'], os.environ['CLOUDANT_PASSWORD'],
                          url=os.environ['CLOUDANT_URL'], connect=True, auto_renew=True)
        database = client.create_database(db_name)
    elif os.path.isfile('vcap-local.json'):
        with open('vcap-local.json') as f:
            vcap = json.load(f)
            print('Found local VCAP_SERVICES')
            creds = vcap['cloudantNoSQLDB'][0]['credentials']
            user = creds['username']
            #password = creds['password']
            apikey = creds['apikey']
            iam_apikey_name = creds['iam_apikey_name']
            url = 'https://' + creds['host']
            # client = Cloudant(user, password, url=url, connect=True)
            # database = client.create_database(db_name)



def get_database():
    print(database)
    return client['gol_data']


def set_database(db):
    global database
    database = db


def disconnect():
    global client
    if client:
        client.disconnect()
