class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
       return f"Start Engine in {self.brand} !"

    @classmethod
    def show_count_of_wheels(cls):
        return cls.wheels

    @staticmethod
    def show_count_doors():
        return 4

car_1 = Car(brand="BMW")
car_2 = Car(brand="Mazda")

# print(Car.wheels)
# print(car_1.wheels)
# print(car_1.brand)
# print(car_1.start_engine())

print(car_1.start_engine())
print(car_2.start_engine())