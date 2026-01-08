"""
Unit Tests for Feature Engineering.
Tests the hashing logic consistency and ranges.
"""
from src.feature_eng import hash_feature

def test_hashing_consistency():
    """
    Test that the same input always produces the same hash.
    """
    assert hash_feature("Istanbul") == hash_feature("Ankara")

def test_hashing_range():
    """
    Test that the hash output is within the specified bucket range.
    """
    result = hash_feature("Ankara", n_buckets=50)
    assert 0 <= result < 50

def test_different_inputs():
    """
    Test that different inputs produce different hashes (usually).
    """
    assert hash_feature("Istanbul") != hash_feature("Izmir")
