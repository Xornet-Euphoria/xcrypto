from math import gcd
from xcrypto.util import prod, list_gcd


def inv(x, n):
    return pow(x, -1, n)


def ext_euclid(a, b):
    x_0, x_1, y_0, y_1 = 1, 0, 0, 1
    sign = 1
    while b != 0:
        r = a % b
        q = a // b
        a = b
        b = r
        tmp_x = x_1
        tmp_y = y_1
        x_1 = q * x_1 + x_0
        y_1 = q * y_1 + y_0
        x_0 = tmp_x
        y_0 = tmp_y
        sign = -sign

    g = a
    # a * (sign*x_0) + b * (-sign*y_0) = g
    return (sign * x_0, -sign * y_0, g)


# chinese reminder theorem
def crt(problem):
    eq_count = len(problem)
    a_list = [x[0] for x in problem]
    m_list = [x[1] for x in problem]

    for i in m_list:
        for j in m_list:
            if i == j:
                continue
            if gcd(i, j) != 1:
                raise ValueError("any 2 modulo pair must be coprime each other")

    m_all_prod = prod(m_list)
    m_star_list = [m_all_prod // m for m in m_list]

    t_list = [ext_euclid(m_list[i], m_star_list[i])[1]
              for i in range(eq_count)]

    answer = 0
    for i in range(eq_count):
        answer += (a_list[i] * m_star_list[i] * t_list[i])

    return answer % m_all_prod
