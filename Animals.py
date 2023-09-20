class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} says Animal"
    def reply(self):
        return f'{self.name} says Meow!'

class Mammal(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
    def speak(self):
        return Animal.speak(self)
class Cat(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, name)
    def speak(self):
        Mammal.reply(self)
        return f'{self.name} says Meow!'
class Dog(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, name)
    def speak(self):
        word = "Woof"
        return f"{self.name} says {word}!"
class Primate(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, name)
    def speak(self):
        word = "Hi"
        return f"{self.name} says  {word}!"
class ComputerScientist(Primate):
    def __init__(self, name):
        Primate.__init__(self, name)
   






   





