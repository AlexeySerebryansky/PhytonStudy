from copy import deepcopy

lst = [0, 1, 7, 2, 4, 8]

lst2 = deepcopy(lst[0::2])
result = sum(lst2) * lst[-1]
print(result)