"""
Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib,
lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin.
Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
"""


def user(name, surname, date, address, number, email=None):
    """
    :param name:
    :param surname:
    :param date:
    :param address:
    :param number:
    :param email:
    :return:
    """
    mijoz = {
        'name': name,
        'surname': surname,
        'date': date,
        'age': 2022 - date,
        'address': address,
        'number': number,
        'email': email
    }
    return mijoz

# print(foydalanuvchi('Ogabek', 'Baxshullayev', 2002, 'Buxoro', 996699069))
