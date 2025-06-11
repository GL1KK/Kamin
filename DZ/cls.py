class Animal:
    def make_sound(self):
        print("Животное издает звук")

class Dog(Animal):
    def make_sound(self):
        print("Гав-гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу-мяу!")


animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()
dog.make_sound()
cat.make_sound()
