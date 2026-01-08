import hashlib


def hash_feature(value, n_buckets=1000):

    if not isinstance(value, str):
        value = str(value)

    encoded = value.encode('utf-8')
    hash_object = hashlib.md5(encoded)
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16) % n_buckets