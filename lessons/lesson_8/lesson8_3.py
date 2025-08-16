# def recur_func():
#     print("!")
#     recur_func()
# recur_func()
from tokenize import group


# def factorial(number: int):
#     if number == 1 or number == 0:
#         return 1
#     else:
#         return number * factorial(number -1)
#
# print(factorial(10))





def double(number : int) -> int :
    return number * 2

print((lambda number: number*2)(11))
print(double(11))



chek_even = lambda x: True if x%2 == 0 else False

print(chek_even(11))
print(chek_even(12))

numbers = [1, 2, 3, 4, 5]

result = list(map(double, numbers))
result2 = list(map(lambda  number: number**2 , numbers))

print(result)
print(result)

result3 = list(filter(lambda x: True if x%2 == 0 else False, numbers))
print(result3)

names = ["Anna", "Vadym", "Masha"]
age = [11, 22, 40]
groups = ("PM-14-01", "PZ-12-2", "PK-11-5")
result_4 = list(zip(names, age, groups))
print(result_4)