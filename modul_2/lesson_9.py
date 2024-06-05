# def full_name(first_name, last_name):
#     result = f"{first_name} {last_name}"
#     return result
#
#
# ism_familiya = full_name("Shohruh", "Abdurahmon")
#
# age = 14
# address = "Sergili"
#
# print(f"{ism_familiya} ning\n"
#       f"yoshi {age} da,{address} da yashaydi")
#
# def age_counter(birth_date, current_year=2024):
#     res = current_year - birth_date
#     return res
#
#
# age = age_counter(birth_date=2010, current_year=2024)
#
# name = "Shohruh"
# address = "Namangan"
#
# print(f"{name} ning yoshi {age} da, manzili {address}")

# def new_range(minimum, maximum):
#     numbers = []
#     while minimum < maximum:
#         numbers.append(minimum)
#         minimum += 1
#
#     return numbers
#
#
# for number in new_range(1, 10):
#     print(number)


def summa(*numbers):
    res = 0
    print(numbers)
    for number in numbers:
        res += number
    return res


print(summa(10, 20, 30, 40, 50, 15))
