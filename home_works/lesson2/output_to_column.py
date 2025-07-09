number = int(input('Enter your 4 digit number : '))


CONST1000 = 1000
CONST100 = 100
CONST10 = 10

number1 = number//CONST1000
number2 = (number % CONST1000 - number % CONST100) // CONST100
number3 = (number % CONST100 - number % CONST10) // CONST10
number4 = number % CONST10

print(number1)
print(number2)
print(number3)
print(number4)

