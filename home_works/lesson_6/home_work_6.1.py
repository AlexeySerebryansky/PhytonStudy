import string

user_input = str(input("Enter your laters : "))

start, end = user_input.split('-')

letters = string.ascii_letters

start_index = letters.index(start)
end_index = letters.index(end)

result = letters[start_index:end_index + 1]
print(result)