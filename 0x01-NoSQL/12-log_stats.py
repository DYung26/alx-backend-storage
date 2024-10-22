#!/usr/bin/env python3

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
nginx_collection = client.logs.nginx

print(f'''{nginx_collection.count_documents({})} logs
Methods:
    method {nginx_collection.count_documents({"method": "GET"})}
    method {nginx_collection.count_documents({"method": "POST"})}
    method {nginx_collection.count_documents({"method": "PUT"})}
    method {nginx_collection.count_documents({"method": "PATCH"})}
    method {nginx_collection.count_documents({"method": "DELETE"})}
{nginx_collection.count_documents({"method": "GET", "path": "/status"})} status check''')
