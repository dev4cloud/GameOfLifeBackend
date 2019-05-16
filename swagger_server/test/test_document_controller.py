# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.entry import Entry  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDocumentController(BaseTestCase):
    """DocumentController integration test stubs"""

    def test_add_document(self):
        """Test case for add_document

        Add a new document
        """
        body = Entry(title="My document", body="a lot of text and much more")
        response = self.client.open(
            '/v2/document',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        print(response.data)

    def test_delete_document(self):
        """Test case for delete_document

        Deletes a document
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/v2/document/{documentId}'.format(documentId=789),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_documents(self):
        """Test case for get_all_documents

        Get all documents
        """
        response = self.client.open(
            '/v2/document',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_document_by_id(self):
        """Test case for get_document_by_id

        Find document by ID
        """
        response = self.client.open(
            '/v2/document/{documentId}'.format(documentId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_document(self):
        """Test case for update_document

        Update an existing document
        """
        body = Entry()
        response = self.client.open(
            '/v2/document',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_document_with_form(self):
        """Test case for update_document_with_form

        Updates a document in the store with form data
        """
        data = dict(name='name_example',
                    status='status_example')
        response = self.client.open(
            '/v2/document/{documentId}'.format(documentId=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
