print("Enter 'yes' if you want to start the calculations.")
start_stop = str(input())

while start_stop == "yes":
    print("Input you first number : ")
    number1 = int(input())
    print("Input you second number : ")
    number2 = int(input())
    print("Input you operator : ")
    action = str(input())

    if action == "+":
        print(number1, " + ", number2, ' = ', number1 + number2)
    elif action == "-":
        print(number1, " - ", number2, ' = ', number1 - number2)
    elif action == "*":
        print(number1, " * ", number2, ' = ', number1 * number2)
    elif action == "/":
        if number2 == 0:
            print("It's not right to divide by zero(((")
        else:
            print(number1, " / ", number2, ' = ', number1 / number2)
    else:
        print("Something went wrong. Maybe you entered the data incorrectly.")
    print("Do you want to sell the calculations?")
    print("Input - Yes, or - No: ")
    start_stop = input()
else:
    print("Buy")

