#!/usr/bin/env python3
"""
This script connects to a MongoDB instance and retrieves logs from the nginx
collection.
It counts the total number of logs and the number of requests for each HTTP
method, as well as the number of status check requests. It then aggregates and
displays the top 10 IPs based on the total number of requests made.
"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx

print(f'''{collection.count_documents({})} logs
Methods:
    method {collection.count_documents({"method": "GET"})}
    method {collection.count_documents({"method": "POST"})}
    method {collection.count_documents({"method": "PUT"})}
    method {collection.count_documents({"method": "PATCH"})}
    method {collection.count_documents({"method": "DELETE"})}
{collection.count_documents({"method": "GET", "path": "/status"})} status check
IPs:''')
ip_counts = collection.aggregate([
    {'$group': {'_id': '$ip', 'totalRequests': {'$sum': 1}}},
    {'$sort': {'totalRequests': -1}},
    {'$limit': 10}
])

for log in ip_counts:
    print(f"    {log['_id']}: {log['totalRequests']}")
