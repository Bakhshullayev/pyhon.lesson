# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing

ismlar = ['Bekhruz', 'Umid', 'Firdavs', 'Anvar', 'Sunnat']
for ism in ismlar:
    print(f'Salom {ism} bugun seni dam olishga taklif qilaman')

print('Hurmat bilan Og\'abek')

# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi"
# degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)

ismlar = ['Bekhruz', 'Umid', 'Firdavs', 'Anvar', 'Sunnat']
for ism in ismlar:
    print(f'Salom {ism} bugun seni dam olishga taklif qilaman')

print('Hurmat bilan Og\'abek')
print(f'Kod {len(ism)} marta takrorlandi')

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing.
# Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.

for son in range(1, 100, 2):
    print(f'{son} ning kubi {son ** 3} ga teng')

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling.
# Natijani konsolga chiqaring.

kinolar = []
for kino in range(5):
    kinolar.append(input(f' {kino + 1} eng sevimli kinongiz qaysi'))

print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang,
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

suhbat = int(input('Bugun nechta odam bilan uchrashdiz ?\n>>>'))
suhbatdoshlar = []
for ism in range(suhbat):
    suhbatdoshlar.append(input(f'{ism + 1}-suhbat qilgan odamingiz kim edi'))

print(suhbatdoshlar)
