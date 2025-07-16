lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

length = len(lst)

for i in range(length):
    index = lst.index(0)
    lst.insert(length, lst.pop(index))

print(lst)

