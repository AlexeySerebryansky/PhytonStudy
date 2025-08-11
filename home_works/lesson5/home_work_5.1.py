input_number = 999

dict_of_numbers = {}

while input_number>0:
   dict_of_numbers = dict_of_numbers.fromkeys([], input_number % 10)

print(dict_of_numbers)