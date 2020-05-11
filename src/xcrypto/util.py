from binascii import unhexlify
from functools import reduce
from math import gcd, ceil
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


# return integer number less than or equal to pow(x, (1/n))
def int_nth_root(x, n):
    b_length = x.bit_length()
    ret_ceil = pow(2, ceil(b_length / n))
    ret_range = [1, ret_ceil]
    while True:
        ret_half = (ret_range[0] + ret_range[1]) // 2
        v = pow(ret_half, n)
        if v < x:
            if pow(ret_half + 1, n) > x:
                return ret_half
            ret_range[0] = ret_half
        elif v > x:
            ret_range[1] = ret_half
        elif v == x:
            return ret_half


def int_sqrt(x):
    return int_nth_root(x, 2)


def is_square(x):
    if x < 0:
        return False

    r = int_sqrt(x)

    return r**2 == x


def fermat_method(n):
    a = int_sqrt(n)

    if a**2 == n:
        return (a, a)

    a += 1
    b_pow_2 = a ** 2 - n

    while not is_square(b_pow_2):
        a += 1
        b_pow_2 = a ** 2 - n

    b = int_sqrt(b_pow_2)

    return (a + b, a - b)
