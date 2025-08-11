def common_elements() -> set:
    three_set = set()
    five_set = set()

    for i in range(101):
        if i % 3 == 0:
            three_set.add(i)

    for i in range(101):
        if i % 5 == 0:
            five_set.add(i)

    intersection_set = three_set.intersection(five_set)

    return intersection_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Ok")