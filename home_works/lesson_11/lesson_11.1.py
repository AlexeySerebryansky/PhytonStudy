from typing import Iterator
import math

def prime_generator(end: int) -> Iterator[int]:
    for number in range(2, end + 1):
        result = True
        for x in range(2, int(math.sqrt(number)) + 1):
            if number % x == 0:
                result = False
                break
        if result:
            yield number


from inspect import isgenerator


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')