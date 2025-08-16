
lst = []
if len(lst) < 1:
    print(lst)
else:
    lst2 = lst[0::2]
    result = sum(lst2) * lst[-1]
    print(result)
