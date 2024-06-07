# import random
#
# taxminiy_son = random.randint(1, 10)
# print(taxminiy_son)

# my_list = ["apple", "banana", "cherry"]
# meva = random.choice(my_list)
# print(meva)

# for _ in range(5):
#     print(random.randint(15, 50))

# from colorama import Fore
#
# print(Fore.BLUE + "Hello World")
# print("Hello World" + Fore.RESET)
# print("Hello World")
# print("Hello World")


from PIL import Image

rasm = Image.open('img_1.png')
print(rasm.show())
