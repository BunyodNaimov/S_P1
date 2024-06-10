from sozlar import inglizcha_uzbekcha, uzbekcha_inglizcha

print("""
    O'zbekcha inglizcha tarjimon dasturimizga xush kelipsiz!
""")

til = input("""
1 -> o'zbekcha
2 -> inglizcha
Tilni tanlang: 
""")

while True:
    tarjima = ""

    soz = input("tarjima qilimoqchi bo'lgan so'zni kiriting: ").lower()

    if til == '1':
        tarjima = inglizcha_uzbekcha.get(soz, "Not Found")
    if til == '2':
        tarjima = uzbekcha_inglizcha.get(soz, "Topilmadi")
    print(f"Tarjima: {tarjima}")
