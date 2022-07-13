"""
Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring.
Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

"""
from lesson20.task_1 import user
mijozlar = []

# while not input("Dasturni to'xtatish uchun q harfini kiriting: ").startswith('q'):
#     name = input("Ism -> ")
#     surname = input("Familiya -> ")
#     date =  input('Yilingiz ->')
#     address = input('Manzilingiz ->')
#     number = input("Tel raqamingiz ->")
#     email = input("Emailingiz  ->")
#
#     mijozlar.append(user(name, surname, int(date) , address, number, email))
#
# print(mijozlar)
while True:
    name = input("Ism -> ")
    surname = input("Familiya -> ")
    date =  input('Yilingiz ->')
    address = input('Manzilingiz ->')
    number = input("Tel raqamingiz ->")
    email = input("Emailingiz  ->")
    mijozlar.append(user(name, surname, int(date), address, number, email))
    javob = input('dasturni to\'xtatmoqchi bo\'lsangiz yes/no')
    if javob != 'no':
        break
print(mijozlar)




