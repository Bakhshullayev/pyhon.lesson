# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

def malumot(ism, t_yil):
    print(f'{ism.title()} siz {2022 - t_yil} yoshda')

malumot(ism='ogabek', t_yil=2002)

# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

def kvadrat_va_kub(son):
    print(son ** 2)
    print(son ** 3)

kvadrat_va_kub(4)

# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

def juft_toq(son):
    if son % 2:
        print('toq son')
    else:
        print("juft son")

juft_toq(3)

# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def katta_kichik(son_1, son_2):
    if son_1 > son_2:
        print(son_1, '>', son_2)
    elif son_1 < son_2:
        print(son_1, '<', son_2)
    elif son_1 == son_2:
        print('sonlar teng')

katta_kichik(10, 5)

# Foydalanuvchidan x va y sonlarini olib,(x ning y darajasi) ni konsolga chiqaruvchi funksiya yozing.

def func_1(x, y=2):
    print(x, 'ning', y, 'darajasi', x ** y, 'ga teng')

func_1(7, 3)

# Foydalanuvchidan son qabul qilib,
# sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing.
# Natijalarni konsolga chiqaring.

def bolinish_alomatlari(son):
    for x in range(2,11):
        if not son%x:
            print(son, x, 'ga qoldiqsiz bo\'linadi')

bolinish_alomatlari(70)
