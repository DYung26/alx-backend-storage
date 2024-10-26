#!/usr/bin/env python3
"""
This module provides a Cache class to interface with Redis,
allowing storage of data with auto-generated unique keys.
It includes methods for storing and retrieving various data types.
"""

import redis
import uuid
from typing import Union


class Cache:
    """A cache system that stores data in Redis with unique keys."""

    def __init__(self):
        """Initialize a connection to the local Redis instance."""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb(True)

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

    def get(self, key, fn):
        """
        Retrieve data from Redis by key, applying an optional transformation
        function.

        Parameters:
        - key (str): The key under which the data is stored.
        - fn (Optional[Callable[[bytes], Union[str, int]]]): A function to
        transform the retrieved data.

        Returns:
        - Optional[Union[str, int]]: The retrieved data after transformation,
        or None if not found.
        """
        return fn(self._redis.get(key)) if fn is not None else self._redis.get(key)

    def get_str(key):
        """
        Retrieve a string value from Redis by key.

        Parameters:
        - key (str): The key under which the string is stored.

        Returns:
        - Optional[str]: The decoded string value, or None if not found.
        """
        self.get(key, lambda x: x.decode('utf-8'))

    def get_int(key):
        """
        Retrieve an integer value from Redis by key.

        Parameters:
        - key (str): The key under which the integer is stored.

        Returns:
        - Optional[int]: The integer value, or None if not found.
        """
        self.get(key, int)