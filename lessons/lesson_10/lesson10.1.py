class Animal:
    paws = 4


class Cat(Animal):

    _year = 1990

    def voice(self):
        print("Meo")


class Dog(Animal):

    def voice(self):
        print("Bark")



def animal_sound(animal: Cat | Dog):
    animal.voice()

cat = Cat()
dog = Dog()

animal_sound(cat)
animal_sound(dog)

# print(cat.paws)
# print(dog.paws)
#
# print(cat.voice())
