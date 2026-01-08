import pytest
from src.feature_eng import hash_feature


def test_hashing_consistency():

    assert hash_feature("Istanbul") == hash_feature("Istanbul")


def test_hashing_range():

    result = hash_feature("Ankara", n_buckets=50)
    assert 0 <= result < 50


def test_different_inputs():

    assert hash_feature("Istanbul") != hash_feature("Izmir")