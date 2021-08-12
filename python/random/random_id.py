import binascii
import os


def random_id():
    return binascii.b2a_hex(os.urandom(8)).decode('utf-8')