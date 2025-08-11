def say_hi(name: str, age: int):

    sentence = f"Hi. My name is {name} and I'm {age} years old"

    return print(sentence)

print("What is your name ?")
name_user = str(input())
print("How old are you?")
age_user = int(input())


say_hi(name_user, age_user)