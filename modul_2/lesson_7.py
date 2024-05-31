# car = {
#     "model": "Lamborjini", "year": 2011, "price": "200.000$", "color": "red"
# }
#
# print(car.keys())
# print(car.get("model"))

# mevalar = {
#     "olma": 10000,
#     "anor": 20000,
#     "uzum": 40000,
#     "anjir": 25000,
#     "shaftoli": 30000,
# }
# for meva in mevalar.values():
#     print(meva)

# phones = {
#     "Iphone 15 Pro": "980$",
#     "Samsung S24 Ultra": "1200$",
#     "Xiaomi Mi 14 Ultra": "1500$"
# }
#
# for phone_name, phone_price in phones.items():
#     print(f"Nomi:{phone_name}-"
#           f"Narxi:{phone_price}")


users = {
    "Botir": {
        "last_name": "Olimov",
        "age": 14,
        "address": "Andijon"
    },
    "Halil": {
        "last_name": "Karimov",
        "age": 12,
        "address": "Qo'qon"
    },
    "Hamid": {
        "last_name": "Sultonov",
        "age": 13,
        "address": "Toshkent"
    }
}

for name, data in users.items():
    print(f"Ismi: {name}\n"
          f"Familiya: {data['last_name']}\n"
          f"Yoshi: {data['age']}\n"
          f"Manzili: {data['address']}\n")
