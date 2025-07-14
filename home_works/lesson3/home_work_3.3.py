import math

lst = [1, 2, 3, 4, 5, 6]
middle_lst = math.ceil(len(lst)/2)
lst1 = lst[:middle_lst:1]
lst2 = lst[middle_lst:]
lst_final = [lst1, lst2]


print(lst_final)