#    ______            __________              __   _____
#   / ____/___  ____  / / ____/ /_  ___  _____/ /__/ ___/__  ______ ___  _____
#  / /   / __ \/ __ \/ / /   / __ \/ _ \/ ___/ //_/\__ \/ / / / __ `__ \/ ___/
# / /___/ /_/ / /_/ / / /___/ / / /  __/ /__/ ,<  ___/ / /_/ / / / / / (__  )
# \____/\____/\____/_/\____/_/ /_/\___/\___/_/|_|/____/\__,_/_/ /_/ /_/____/

#                              Its-Pedram - 2024
#                             https://pedram.tech

import hashlib
from config import ALGORITHMS, CONFIG


def compute(file_path, algorithm):
    hasher = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        while buffer := f.read(CONFIG["buffer_size"]):
            hasher.update(buffer)
    return hasher.hexdigest()


def compute_all(file_path):
    return {algorithm: compute(file_path, algorithm) for algorithm in ALGORITHMS}


def guess_by_length(checksum):
    if len(checksum) == 32:
        return "md5"
    elif len(checksum) == 40:
        return "sha1"
    elif len(checksum) == 56:
        return "sha224"
    elif len(checksum) == 64:
        return "sha256"
    elif len(checksum) == 96:
        return "sha384"
    elif len(checksum) == 128:
        return "sha512"
    else:
        raise ValueError("Could not determine algorithm")


def brute_force(file_path, checksum):
    for algorithm in ALGORITHMS:
        if compute(file_path, algorithm) == checksum:
            return algorithm
    raise ValueError("Could not determine algorithm")


def compare(file_path, checksum, algorithm=None):
    if algorithm is None:
        try:
            algorithm = guess_by_length(checksum)
        except ValueError:
            # This is likely redundant at this time, but may be useful once more algorithms are added
            algorithm = brute_force(file_path, checksum)
    return compute(file_path, algorithm) == checksum
