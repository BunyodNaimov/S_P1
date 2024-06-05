def summa(*numbers):
    res = 0
    print(numbers)
    for number in numbers:
        res += number
    return res


print(summa(10, 20, 30, 40, 50, 15))
