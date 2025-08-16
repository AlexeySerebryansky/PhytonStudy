import random

lst_len = random.randint(3, 10)
print(lst_len)

lst = []

for i in range(lst_len):
    number = int(random.random() * 10)
    lst.append(number)
print(lst)

lst2 = [lst[0], lst[2], lst[-2]]
print(lst2)