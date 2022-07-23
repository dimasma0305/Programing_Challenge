import collections
import itertools
from math import sqrt


def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def get_divisors(n):
    pf = prime_factors(n)

    pf_with_multiplicity = collections.Counter(pf)

    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]

    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)


def list_squared(m, n):
    solution = []
    for i in range(m, n):
        divs = get_divisors(i)
        div_v1 = []
        while True:
            try:
                div_v1.append(next(divs))
            except StopIteration:
                break
        div_v1_sum = sum([int(i**2) for i in div_v1])
        div_v1_sum_sqrt = sqrt(div_v1_sum)
        if div_v1_sum_sqrt.is_integer():
            solution.append([i, int(div_v1_sum)])
    return solution

# from functools import reduce

# def square_factors(n):
#     return set(reduce(list.__add__,
#                      ( [i**2, (n//i)**2] for i in range(1, int(n**0.5) + 1) if n % i == 0) ))
# def list_squared(a, b):
#     ary = []
#     for i in range(a, b + 1):
#         sum_factors = sum(square_factors(i))
#         if (sum_factors**0.5).is_integer():
#             ary.append([i, sum_factors])
#     return ary


import time
# start timer
t0 = time.time()
print(list_squared(1, 250000))
t1 = time.time() - t0
print(t1)