from functools import reduce


def factorial(n):
    """ Calculate factorial with a recursive algorithm. """
    if n <= 1:
        return 1
    return n * factorial(n-1)


def factorial_v2(n):
    """ Calculate factorial with list comprehension, reduce and lambda function. """
    if n <= 1:
        return 1
    parts = [x for x in range(1, n+1)]
    return reduce((lambda x, y: x * y), parts)