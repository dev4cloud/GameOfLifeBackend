import connexion
import six

from swagger_server.models.entry import Entry  # noqa: E501
from swagger_server import util
from swagger_server.database import database


def add_entry(body):  # noqa: E501
    """Add a new entry

     # noqa: E501

    :param body: entry object that needs to be added
    :type body: dict | bytes

    :rtype: None
    """
    print(body)
    if connexion.request.is_json:
        sampleDoc= Entry.from_dict(connexion.request.get_json())  # noqa: E501
        print(sampleDoc)
        db = database.get_database()
        db.create_document(body)
    return "foobar"


def delete_entry(entryId, api_key=None):  # noqa: E501
    """Deletes a entry

     # noqa: E501

    :param entryId: entry id to delete
    :type entryId: str
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    db = database.get_database()
    db[entryId].delete()
    return None


def get_all():  # noqa: E501
    """Get all entrys

    Returns all entrys # noqa: E501

    :param entryId: ID of entry to return
    :type entryId: str

    :rtype: List[entry]
    """
    data = []
    all_docs = database.get_database()
    print(database.get_database())
    print(all_docs)
    for entry in all_docs:
        data.append(Entry.from_dict(entry))
    print(data)
    return data


def get_entry_by_id(entryId):  # noqa: E501
    """Find entry by ID

    Returns a single entry # noqa: E501

    :param entryId: ID of entry to return
    :type entryId: str

    :rtype: Entry
    """
    entry = database.get_database()[entryId]
    return Entry.from_dict(entry)

