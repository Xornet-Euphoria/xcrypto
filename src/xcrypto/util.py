from binascii import unhexlify
from functools import reduce
from math import gcd
from Crypto.Util.number import long_to_bytes


def hexstr_to_str(hex_str):
    return unhexlify(hex_str).decode()


def num_to_str(num):
    return long_to_bytes(num).decode()


def prod(num_list):
    return reduce(lambda x, y: x * y, num_list)


def list_gcd(num_list):
    return reduce(gcd, num_list)