import string
import re
from math import sqrt


def is_pangram(s):

    return set(string.ascii_lowercase) <= set(s.lower())


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))



from time import time, sleep
from functools import wraps

def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f"Time elapsed: {round(end - start, 2)}")
        return result
    return wrapper

@timeit
def foo(timeout):
    """
    This is a foo function.
    """
    sleep(timeout)

if __name__ == "__main__":
    print(foo.__doc__)
    print(foo.__name__)


def fibonacci(n: int) -> int:
    x,y = 0, 1
    for i in range(n):
        x , y = y , y+x
    return x

print(fibonacci(45))

def lru_cache(fn):
    cache = {}

    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = fn(*args, **kwargs)
        return cache[args]
    return wrapper

@timeit
@lru_cache
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print(
        fib(45)
    )

def append_to(element, to=None):
    if to is None:
        return [element]
    to.append(element)
    return to

if __name__ == "__main__":
    my_list = append_to(12)  # to
    print(my_list)

    my_list_2 = append_to(100)  # to
    print(my_list_2)

    my_list_3 = append_to(1000)  # to
    print(my_list_3)


def czy_pierwsza(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(czy_pierwsza(1))

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class PrimeIterator:
    # Iterator pozwalający na iterowanie po n liczbach pierwszych
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()


iter = PrimeIterator(100)
for elem in iter:
    print(elem)