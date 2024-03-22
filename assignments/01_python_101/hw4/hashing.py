import hashlib
from typing import Any


def hash_input(input: Any) -> str:
    input_bytes = str(input).encode('utf-8')
    hash_object = hashlib.sha256(input_bytes)
    hash_hex = hash_object.hexdigest()
    return hash_hex
