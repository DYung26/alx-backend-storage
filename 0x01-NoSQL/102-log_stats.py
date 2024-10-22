#!/usr/bin/env python3
"""
This script connects to a MongoDB instance and retrieves logs from the nginx
collection.
It counts the total number of logs and the number of requests for each HTTP
method, as well as the number of status check requests. It then aggregates and
displays the top 10 IPs based on the total number of requests made.
"""
from pymongo import MongoClient


def main():
    """
    Connects to the MongoDB database and initiates the log statistics
    retrieval.

    This function creates a connection to the MongoDB server running on
    localhost and calls the log_stats() function to print out the statistics
    of the NGINX logs.

    Returns:
        None
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_stats(client.logs.nginx)


def log_stats(cllctn):
    """
    Prints statistics about HTTP requests logged in the specified MongoDB
    collection.

    This function retrieves and displays the total number of logs, counts for
    each HTTP method (GET, POST, PUT, PATCH, DELETE), and the number of status
    check requests made to the "/status" path.

    Args:
        cllctn: The MongoDB collection object containing the NGINX logs.

    Returns:
        None
    """
    print(f'''{cllctn.count_documents({})} logs
Methods:
    method GET: {cllctn.count_documents({"method": "GET"})}
    method POST: {cllctn.count_documents({"method": "POST"})}
    method PUT: {cllctn.count_documents({"method": "PUT"})}
    method PATCH: {cllctn.count_documents({"method": "PATCH"})}
    method DELETE: {cllctn.count_documents({"method": "DELETE"})}
{cllctn.count_documents({"method": "GET", "path": "/status"})} status check''')
    ip_counts = collection.aggregate([
        {'$group': {'_id': '$ip', 'totalRequests': {'$sum': 1}}},
        {'$sort': {'totalRequests': -1}},
        {'$limit': 10}
    ])

    for log in ip_counts:
        print(f"    {log['_id']}: {log['totalRequests']}")


if __name__ == '__main__':
    main()
