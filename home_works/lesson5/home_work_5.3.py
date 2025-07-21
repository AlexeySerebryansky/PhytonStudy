import re
print("Enter your text :")
input_string = str(input())

# input_string = re.sub('[?!@#$.,]', '', input_string)

input_string = input_string.replace(",", "")
input_string = input_string.replace(".", "")
input_string = input_string.replace("?", "")
input_string = input_string.replace("!", "")

input_string = input_string.title()
input_string = input_string.replace(" ", "")

input_string = input_string[:140]
print("#" + input_string)





