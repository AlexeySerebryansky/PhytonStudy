# def test_func():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
#
# # generator = test_func()
# # print(generator)
# # print(next(generator))
# # print(next(generator))
# # print(next(generator))
# # print(next(generator))
#
# for elem in test_func():
#     print(elem)



def fibonacchi_generarot(iterations: int):
    a, b = 0, 1
    count = 0
    while count < iterations:
        yield  a
        a, b = b, a + b
        count += 1


generator = fibonacchi_generarot(10)

for number in generator:
    print(number)