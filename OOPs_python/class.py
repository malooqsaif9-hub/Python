# class Animal:
#     type  = "cat"# attribute

#     def sound(self): # method
#         print("meow")

# print(Animal().type)

# Animal().sound()

# # now we see how objects are created 
# obj = Animal()
# print(obj.type)
# obj.sound()

#  obj2 =  Animal()


# class Factory:
#     def __init__(self,materials,zips,pockets):
#         self.materials = materials #instance attribute
#         self.zips = zips
#         self.pockets = pockets


# reebok = Factory("leather",3,2)
# campus = Factory("nylon",4,2)
# print(reebok.pockets)

class Demo:
    class_var = " i am a class variable"

    def __init__ (self,value):
        self.value = value

    def instance_method(self):
        return self.value
    
    @classmethod
    def class_method(cls):
        return cls.class_var
    
    @staticmethod
    def static_method():
        return "i dont use any self or cls "
    
obj = Demo(19)
print(obj.instance_method())
print(Demo.class_method())
print(Demo.static_method())
        
