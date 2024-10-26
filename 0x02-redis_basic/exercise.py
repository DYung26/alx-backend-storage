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

    def get(
            self,
            key: str,
            fn: Optional[Callable[[bytes], Union[str, int]]] = None
            ) -> Optional[Union[str, int]]:
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
        byte_string = self._redis.get(key)
        return fn(byte_string) if fn is not None else byte_string

    def get_str(key: str) -> Optional[str]:
        """
        Retrieve a string value from Redis by key.

        Parameters:
        - key (str): The key under which the string is stored.

        Returns:
        - Optional[str]: The decoded string value, or None if not found.
        """
        self.get(key, lambda x: x.decode('utf-8'))

    def get_int(key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis by key.

        Parameters:
        - key (str): The key under which the integer is stored.

        Returns:
        - Optional[int]: The integer value, or None if not found.
        """
        self.get(key, int)
