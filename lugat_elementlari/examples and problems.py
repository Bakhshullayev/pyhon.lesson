# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida,
# alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.

python_org = {
    'integer': 'butun son',
    'float': 'o\'nlik son',
    'string': 'matn',
    'get()': 'yangi qiymat qo\'shish ',
    '.len()': 'qiymatni uzunligini aniqlash'
}
for key, value in sorted(python_org.items()):
    print(f'{key.title()} bu  {value} deb ataladi')

# Davlatlar va ularning poytaxtlari lug'atini tuzing.
# Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida,
# alifbo ketma-ketligida konsolga chiqaring.

countries = {
    'uzbekistan': 'Toshkent',
    'rossiya': 'Moskva',
    'ukraina': 'Kiyev',
    'ruminiya': 'Buxarest',
    'fransiya': 'Parif'
}
for key, value in sorted(countries.items()):
    print(f" {key.title()}     {value} ")

# Foydalanuvchidan istalgan davlatni kiritishni so'rang
# shu davlatning poytaxtini konsolga chiqaring.
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

states = {
    'uzbekistan': 'Toshkent',
    'rossiya': 'Moskva',
    'ukraina': 'Kiyev',
    'ruminiya': 'Buxarest',
    'fransiya': 'Parif'
}
davlat = input('Biror davlatni kiriting').lower()
print(states.get(davlat, 'Bizda bunday malumot yoq'))

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang.
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring,
# agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

restoran = {
    'non': 3000,
    'osh': 20000,
    'somsa': 7000,
    'cola': 12000,
    'salat': 8000,
    'norin': 25000,
    'qozon kabob': 60000
}
print("3 ta taom buyurtma bering")
buyurtmalar = []
for ovqat in range(3):
    buyurtmalar.append(input(f'{ovqat + 1} - taomni qoshing'))
for buyurtma in buyurtmalar:
    if buyurtma in restoran:
        print(f'{buyurtma.title()} {restoran[buyurtma]} som')
    else:
        print(f'kechirasiz bizda bunday {buyurtma.title()}mavjud emas')
