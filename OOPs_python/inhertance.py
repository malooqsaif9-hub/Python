# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound ")

#     def eating(self):
#         print(f"{self.name} is eating ")

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} barks")

# obj = Dog("Brunno")
# obj.bark()
# obj.eating()
# obj.speak()        


#super() — Calling Parent's Constructor

class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"the name is {self.name} and the age is {self.age}and the breed is {self.breed}")

class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed        

d = Dog("brunno",3,"lebrador")
print(d.show())
print(d.breed)
Animal.show() # this gives error 