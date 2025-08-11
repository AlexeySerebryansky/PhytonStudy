print("Input your number")
input_number = int(input())

while input_number > 9:
    product = 1
    for i in str(input_number):
        product *= int(i)
    input_number = product

print(input_number)


