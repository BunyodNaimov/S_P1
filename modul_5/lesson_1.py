# class Car:
#     def __init__(self, model, color, year, price):
#         self.model = model
#         self.color = color
#         self.year = year
#         self.price = price
#
#
# bmw = Car("BMW", "White", 2024, 100000)
# gentra = Car("Gentra", "Black", 2020, 10000)
# malibu = Car(model="Malibu", color="White", year=2020, price="13.000$")
# print(f"Model: {bmw.model}\n"
#       f"Rangi: {bmw.color}\n"
#       f"Yili: {bmw.year}")

class Student:
    def __init__(self, name, age, address, current_year=2024):
        self.name = name
        self.age = age
        self.address = address
        self.current_year = current_year

    def get_date(self):
        return (f"{self.name} ning yoshi {self.age} da \n"
                f"Yashash Manzili: {self.address}")

    def get_age(self, year):
        return f"{self.name} ning yoshi {self.current_year - year}"


abdulla = Student(name="Abdulla", age=15, address="Buxoro")
anvara = Student(name="Anvara", age=15, address="San Francisco")
print(abdulla.get_age(2010))
print(anvara.get_date())
