def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


print(fib(20))

from functools import lru_cache


@lru_cache()
def fib2(n):
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)


print(fib2(20))
