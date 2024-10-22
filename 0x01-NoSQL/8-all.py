#!/usr/bin/env python3
'''
Module to interact with MongoDB collections.

This script contains a function to list all documents in a specified MongoDB
collection.
'''


def list_all(mongo_collection):
    """
    List all documents in a given MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection from which to retrieve documents.

    Returns:
        list: A list of documents. Returns an empty list if no documents are
        found.
    """
    documents = list(mongo_collection.find()) or []
    return documents
