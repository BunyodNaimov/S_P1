# class Father:
#     def __init__(self, last_name, address):
#         self.last_name = last_name
#         self.address = address
#
#     def get_date(self):
#         return f"{self.last_name} ning, manzili {self.address}  "
#
#
# class Son(Father):
#     def __init__(self, last_name, address, name, age):
#         super().__init__(last_name, address)
#         self.name = name
#         self.age = age
#
#
# son = Son("Beknazarova", "Qarshi", "Yulduz", 18)
# print(son.address)
# print(son.name)
# print(son.age)
# print(son.get_date())


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         pass
#
#
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof"
#
#
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow"
#
#
# dog = Dog("Qoplon", 2)
# cat = Cat("Felix", 3)
#
# print(cat.name)
# print(dog.age)
# print(dog.speak())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def get_name(self):
        return self.name


class Doctor(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job


class Policeman(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job


doctor = Doctor("Anvar", 30, "Stamatolog")
policeman = Policeman("Abdulla", 30, "Axrana")
print(doctor.job)
print(policeman.job)
print(policeman.get_name)
