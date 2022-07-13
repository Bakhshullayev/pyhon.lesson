# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib,
# lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin.
# Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

def foydalanuvchi(name, surname, date, manzil, email=None, number=''):
    '''Mijoz haqidagi funksiyani lugat korinishida qaytaruvchi funksiya'''
    mijoz = {
        'name': name,
        'surname': surname,
        'date': date,
        'manzil': manzil,
        'email': email,
        'number': number
    }
    return mijoz


mijozlar = []
while True:
    name = input('isminigizni kiriting').title(),
    surname = input('familyangizni kiriting').title(),
    date = input('yoshingizni kiting'),
    manzil = input('manzilingizni kiriting'),
    email = input('emailingizni kiriting'),
    number = input('telefon raqamingizni kiriting')
    mijozlar.append(foydalanuvchi(name, surname, date, manzil, email, number))
    javob = input('davom etasizmi ha/yoq')
    if javob != 'ha':
        break
print('Mijozlarimiz')
for mijoz in mijozlar:
    print(f"{mijoz['name']}, {mijoz['surname']},"
          f"{mijoz['date']} , nomeri {mijoz['number']},"
          f"{mijoz['email']}")

# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring.
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

