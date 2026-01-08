"""
Feature Engineering Module.
This module contains functions to transform raw data into features for the model.
"""


def hash_feature(value, n_buckets=1000):
    """
    Hashes a string value into a numerical bucket.

    Args:
        value (str): The input string to hash.
        n_buckets (int): The number of buckets (default 1000).

    Returns:
        int: The bucket index.
    """
    return hash(value) % n_buckets
