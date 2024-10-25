#!/usr/bin/env python3
"""
This module provides a Cache class to interface with Redis,
allowing storage of data with auto-generated unique keys.
"""

import redis
import uuid
from typing import Union


class Cache:
    """A cache system that stores data in Redis with unique keys."""

    def __init__(self):
        """Initialize a connection to the local Redis instance."""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a unique UUID key.

        Parameters:
        - data (Union[str, bytes, int, float]): The data to be stored in Redis.

        Returns:
        - str: The UUID key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
