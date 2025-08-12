# def test_func(a: int | float, b) -> int | str | bool:
#     return a + b

# lst = [1, 2, 3]
#
# summ = sum(lst)

# def sum_func(*args):
#     summ = 0
#     for elem in args:
#         summ += elem
#
#     return summ
# print(sum_func(1, 2, 3, 4))


# def sum_func (**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
# print(sum_func(name = "masha", age = 10, group = "PM-14-1" ))


def sum_func(first_arg, second_arg):
    print(first_arg)
    print(second_arg)
    return first_arg
#
# new_int = 10
# old_int = new_int
# print(sum_func(new_int, 2))

new_func = sum_func
print(new_func(1, 2))