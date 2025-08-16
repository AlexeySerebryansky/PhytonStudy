import string

print("Enter your text :")
input_string = str(input())

input_string = ''.join(char for char in input_string if char not in string.punctuation)

input_string = input_string.title()
input_string = input_string.replace(" ", "")
input_string = input_string[:140]

print("#" + input_string)





