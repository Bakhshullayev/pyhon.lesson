"""Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
Talabaning ismi va familiyasi majburiy argument,
qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin."""

def foydalanuvchi(ism, familya,**malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familya'] = familya
    return malumotlar
print(foydalanuvchi('ogabek'.title(),'baxshullayev'.title(),yosh = 20, manzil = 'Buxoro viloyati'))