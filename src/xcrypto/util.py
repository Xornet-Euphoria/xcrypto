from binascii import unhexlify
from functools import reduce
from math import gcd
from Crypto.Util.number import long_to_bytes


def hexstr_to_str(hex_str):
    return unhexlify(hex_str).decode()


def num_to_str(num):
    return long_to_bytes(num).decode()


# if UnicodeDecodeError is raised, error message (default is "decode error") is dumped
def dump_hex_str(hex_str, msg="decode error"):
    try:
        res = hexstr_to_str(hex_str)
        print(res)
    except:
        print(msg)


def dump_num(num, msg="decode error"):
    try:
        res = num_to_str(num)
        print(res)
    except:
        print(msg)


def prod(num_list):
    return reduce(lambda x, y: x * y, num_list)


def list_gcd(num_list):
    return reduce(gcd, num_list)
