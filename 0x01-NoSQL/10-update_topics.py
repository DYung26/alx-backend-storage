#!/usr/bin/env python3
"""
Module to interact with MongoDB collections for school documents.

This module provides functions to update school documents in a MongoDB
collection, including updating the topics associated with a specific school
name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection to update.
        name (str): The name of the school document to update.
        topics (list): The list of topics to set for the school document.

    Returns:
        UpdateResult: The result of the update operation.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
