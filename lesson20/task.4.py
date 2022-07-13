"""Foydalanuvchidan aylaning radiusini qabul qilib olib,
uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing"""

def aylana_yuzi(radius, pi=3.14159):
    aylana = {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * radius * pi,
        "yuza": pi * radius ** 2,
    }
    return aylana
print(aylana_yuzi(3))