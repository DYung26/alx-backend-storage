#!/usr/bin/env python3
"""
Module to interact with MongoDB collections.

This script contains a function to insert a school document into a specified
MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a school document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection where the document will be inserted.
        **kwargs: Keyword arguments representing the fields of the school
        document to be inserted.

    Returns:
        ObjectId: The _id of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
