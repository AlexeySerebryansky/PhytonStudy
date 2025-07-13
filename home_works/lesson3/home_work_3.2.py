lst = [1, 2, 3, 4, 5, 6 ]

print(lst)

lst.insert(0, lst[-1])
lst.append(lst[1])
lst.pop(-2)
lst.pop(1)

print(lst)