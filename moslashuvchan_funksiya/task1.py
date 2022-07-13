"""Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing"""


def kopaytma(*sonlar):
    """istalgancha sonlarni ko'paytmasini chiqaruvchi dastur"""
    number = 1
    for son in sonlar:
        number *= son
    return number


print(kopaytma(2, 4, 5, 5, 5))
