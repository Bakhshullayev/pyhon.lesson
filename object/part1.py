"""Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
get_info() metodi avti haqida to'liq ma'lumotni matn ko'rinishida qaytarsin"""


class Avto():
    """avto nomli yangi funksiya"""

    def __init__(self, model, color, karobka, narh):
        self.model = model
        self.color = color
        self.karobka = karobka
        self.narh = 30000
        self.km_yangilanish = 1

    def get_update(self):
        """Avto yangilanganligi haqida xabar beradi"""
        self.km_yangilanish += 1

    def rusumi(self):
        """Avtoning rusumi"""
        return self.model

    def rang(self):
        """Avtoning rangi"""
        return self.color

    def box(self):
        """Avtoning karobkasi"""
        return self.karobka

    def get_malumot(self):
        """Avto haqida qisqacha malumot"""
        return f"Salonimizdagi avtolar {self.model},{self.color},{self.karobka},{self.narh},{self.km_yangilanish} km yangilandi"


avtolar1 = Avto("GM", "qora", "avtomat", 40000)
avtolar2 = Avto("Nissan", "oq", "avtomat", 50000)
avtolar2.get_update()
print(avtolar1.get_malumot())
print(avtolar2.get_malumot())
print(avtolar2.get_update())
