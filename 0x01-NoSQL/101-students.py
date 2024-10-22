#!/usr/bin/env python3
'''
This module contains a function to calculate and update the average score
for each student in a MongoDB collection. It retrieves student documents,
computes the average score based on their topics, and updates the documents
with the new average score. Finally, it returns the updated student documents
sorted by their average score in descending order.
'''


def top_students(mongo_collection):
    '''
    Calculate and update the average score for each student in a MongoDB
    collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection containing student documents.

    Returns:
        list: A cursor to the updated student documents sorted by their
        average score in descending order.
    '''
    students = mongo_collection.find({})
    for student in students:
        total_score = 0
        count = 0
        for topic in student['topics']:
            total_score += topic['score']
            count += 1
        average_score = total_score / count if count > 0 else 0
        mongo_collection.update_one(
            {'name': student['name']},
            {'$set': {'averageScore': average_score}}
        )
    return mongo_collection.find({}).sort('averageScore', -1)
