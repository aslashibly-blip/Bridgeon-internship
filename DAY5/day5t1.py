class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def speak(self):
        print(self.sound)
class Dog(Animal):
    def speak(self):
        print(f"{self.name}says woof")
class cat(Animal):
    def speak(self):
        print(f"{self.name}says Meow")
d1=Dog("Jimmy","woof")
c1=cat("jerry","Meow")
d1.speak()
c1.speak()