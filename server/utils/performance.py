"""
Performance Optimization
"""

from cachetools import TTLCache
import os

cache = None

def setup_cache():
    """
    Setup cache configuration.
    """
    global cache
    if os.getenv("CACHE_ENABLED") == "true":
        cache = TTLCache(maxsize=100, ttl=int(os.getenv("CACHE_TIMEOUT")))

def get_from_cache(key):
    """
    Get an item from the cache.

    Args:
        key (str): Key of the item to retrieve.

    Returns:
        Any: Cached item, or None if not found.
    """
    return cache[key] if key in cache else None

def set_in_cache(key, value):
    """
    Set an item in the cache.

    Args:
        key (str): Key of the item to cache.
        value (Any): Value of the item to cache.
    """
    if cache is not None:
        cache[key] = value

# Setup cache
setup_cache()
