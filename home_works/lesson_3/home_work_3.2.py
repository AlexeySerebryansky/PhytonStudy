lst = [12, 3, 4, 10, 8]

print(lst)

if len(lst) > 0:
    lst.insert(0, lst.pop())
    print(lst)
else:
    print(lst)


