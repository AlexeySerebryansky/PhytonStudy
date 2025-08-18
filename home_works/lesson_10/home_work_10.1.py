def pow(x: int) -> int:
    return x ** 2

def some_gen(begin: int, end: int, func):
    value = begin
    yield value
    for i in range(end - 1):
        value = func(value)
        yield value


from inspect import isgenerator

gen = some_gen(2, 4, pow)


assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
