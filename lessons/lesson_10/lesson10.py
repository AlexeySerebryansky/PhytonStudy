# with open("text.txt", "a") as file:
#     print(file.write("New world!"))


class Car:
    count_of_wheels = 4

    def __init__(self, name: str):
        self.name = name


first_car = Car("BMW")
second_car = Car(name="Belaz")

print(first_car.name)
print(second_car.name)







# first_car.name = "Mercedes"
#
# print(first_car.name)
#
# first_car.year = 1997
# print(first_car.year)