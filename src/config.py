CCS_VERSION = "3.0.0"
ALGORITHMS = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]

CONFIG = {
    "buffer_size": 65536,
}

import json


def load():
    try:
        with open("config.json", "r") as f:
            CONFIG.update(json.load(f))
    except FileNotFoundError:
        pass
