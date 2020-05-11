from xcrypto.num_util import *


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
