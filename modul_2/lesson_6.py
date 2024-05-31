# car = ["BMW", 2020, "50.000$", "blue"]
#
# car_name = car[0]
# car_year = car[1]
# car_price = car[2]
# car_color = car[3]
#
# print(f"""
# Sevimli moshinam!
#     Nomi: {car_name}
#     Yili: {car_year}
#     Narxi: {car_price}
#     Rangi: {car_color}
# """)
#
# translate = {"Privet": "Hello"}
#
# car_dict = {
#     "model": "BMW",
#     "year": 2020,
#     "price": "50.000$",
#     "color": "Blue"
# }
#
# car_dict["speed"] = "200 km/h"
#
# print(f"""
# Sevimli moshinam!
#     Nomi: {car_dict["model"]}
#     Yili: {car_dict["year"]}
#     Narxi: {car_dict["price"]}
#     Rangi: {car_dict["color"]},
#     Tezligi: {car_dict["speed"]}
# """)
#
#
# user = {
#     "name": "Abdullo",
#     "age": 18,
# }
# user["address"] = "Sergili"
# user["school"] = "8 - maktab"
# user["name"] = "Farxod"
#
# print(f"""
# Mening malumotlarim!
#     Ismim: {user["name"]}
#     Yoshim: {user["age"]}
#     Manzilim: {user["address"]}
#     Maktabim: {user["school"]}
# """)

#
# cat = {
#     "cat": "Kosha",
#     "age": 3
# }
# print(cat)
#
# cat["color"] = "White"
#
# print(cat)
#
# cat["color"] = "Black"
# print(cat)
#
# del cat["age"]
# print(cat)
# print(cat["age"])

cars = [
    {"model": "Lamborjini", "year": 2011, "price": "200.000$", "color": "red"},
    {"model": "Ferrari", "year": 2012, "price": "300.000$", "color": "blue"},
    {"model": "Damas", "year": 2000, "price": "6.000$", "color": "white"},
    {"model": "Nexia 2", "year": 2010, "price": "9.000$", "color": "black"},
]

print(cars[0]["year"])
print(cars[1]["model"])
print(cars[2]["model"])
print(cars[3]["model"])
