
CONST10000 = 10000
CONST1000 = 1000
CONST100 = 100
CONST10 = 10

print("Enter your 5 values number : ")

number = int(input())

number1 = number // CONST10000
number2 = (number // CONST1000) % CONST10
number3 = (number % CONST1000) // CONST100
number4 = (number % CONST100) // CONST10
number5 = (number % CONST10)

print("Your number is : ", number)

print("But its opposite number is : ",
      number5 * CONST10000 + number4 * CONST1000 + number3 * CONST100 + number2 * CONST10 + number1
      )

