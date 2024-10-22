#!/usr/bin/env python3
"""
Module for interacting with a MongoDB collection of schools.

This module provides functions to query school documents from a MongoDB
collection based on specific topics.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve all school documents that contain a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection to query.
        topic (str): The topic to search for within school documents.

    Returns:
        pymongo.cursor.Cursor: A cursor pointing to the documents that match
        the query.
    """
    return mongo_collection.find({"topics": topic})
