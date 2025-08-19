class Animal:
    def speak(self):
        print("Animal speak")

class Dog(Animal):
    def bark(self):
        print("Dog bark")


my_dog = Dog()

my_dog.bark()
my_dog.speak()