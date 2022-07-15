"""Web sahifangiz uchun foydalanuvchi (user) klassini tuzing.
 Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting
 (ism, foydalanuvchi ismi, email, va hokazo)"""


class User():
    """User nomli class yaratamiz"""

    def __init__(self, name, surname, email, number=None):
        self.name = name
        self.surname = surname
        self.email = email
        self.number = number

    def ism(self, ism):
        """Userning ismi"""
        return self.ism

    def familya(self, surname):
        """Userning familyasi"""
        return self.surname

    def elektron_manzil(self, email):
        """Userning elektron manzili"""
        return self.email

    def tel_raqami(self, number):
        """Userning telefon raqami"""
        return self.number

    def kirit(self):
        return f"Foydalanuvchi: {self.ism()},{self.surname},{self.email},{self.number},"


user_1 = User("Ogabek","Baxshullayev","aser669969",996699069)
print(user_1)