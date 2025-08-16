import keyword
import string


print("enter name of your value :")
name_value = str(input())

if name_value in keyword.kwlist:
   print(False)
elif name_value[0].isdigit():
   print(False)
elif any(latters.isupper() for latters in name_value):
   print(False)
elif name_value.count("_") > 1:
   print(False)
elif not name_value:
   print(False)
elif any(char in string.punctuation.replace("_", " ") for char in name_value):
   print(False)
else:
   print(True)


