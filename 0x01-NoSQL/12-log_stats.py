#!/usr/bin/env python3
"""
Script to analyze logs from an NGINX MongoDB collection.

This script connects to a MongoDB database and retrieves various statistics
about the HTTP requests logged in the NGINX collection, including the total
number of logs and the count of each HTTP method used.

Usage:
    python3 script_name.py
"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
cllctn = client.logs.nginx

print(f'''{cllctn.count_documents({})} logs
Methods:
    method GET: {cllctn.count_documents({"method": "GET"})}
    method POST: {cllctn.count_documents({"method": "POST"})}
    method PUT: {cllctn.count_documents({"method": "PUT"})}
    method PATCH: {cllctn.count_documents({"method": "PATCH"})}
    method DELETE: {cllctn.count_documents({"method": "DELETE"})}
{cllctn.count_documents({"method": "GET", "path": "/status"})} status check''')
