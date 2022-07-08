# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang.
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

vohidov = {'ism': 'Erkin Vohidov',
           'tyil': 1936,
           'vyil': 2016,
           'tjoy': "Farg'ona",
           'asarlar': ["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"]
           }

navoiy = {'ism': 'Alisher Navoiy',
          'tyil': 1441,
          'vyil': 1501,
          'tjoy': "Xirot",
          'asarlar': ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", 'Munojot']
          }
adabiyot = [vohidov, navoiy]
for sharq in adabiyot:
    print(f"{sharq['ism']} adabiyotimizning yetuk vakili {sharq['tyil']} da tug'ilganlar. {sharq['tjoy']}"
          f"da tavallud topganlar ")

# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.


vohidov = {'ism': 'Erkin Vohidov',
           'tyil': 1936,
           'vyil': 2016,
           'tjoy': "Farg'ona",
           'asarlar': ["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"]
           }

navoiy = {'ism': 'Alisher Navoiy',
          'tyil': 1441,
          'vyil': 1501,
          'tjoy': "Xirot",
          'asarlar': ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", 'Munojot']
          }
adabiyot = [vohidov, navoiy]
for sharq in adabiyot:
    print(f"{sharq['ism']}ning mashhur asarlari {sharq['asarlar']}")

# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang.
# Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.
# Natijani konsolga chiqaring.

friends = {
    'Bekhruz': 'Forsaj',
    'Mironshoh': 'Deadpool',
    'Shohjahon': 'Aligarx',
    'Umid': 'Summerk',
    'Firdavs': 'Temir odam'
}
for key, value in friends.items():
    print(f"{key} ning sevimli kinosi {value}")

# Davlatlar degan lug'at yarating,
# lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.
# Har bir davlat haqida ma'lumotni konsolga chiqaring.

states = {
    "O'zbekiston": {'poytaxt': "toshkent".title(),
                    'maydon': 448978,
                    'aholi': 33_000_000,
                    'pul birligi': "so'm"
                    },
    "Rossiya": {'poytaxt': "moskva".title(),
                'maydon': 17_098_246,
                'aholi': 144_000_000,
                'pul birligi': "rubl"
                }
}
for davlat, malumot in states.items():
    print(f"{davlat}ning poytaxti {malumot['poytaxt']},maydoni {malumot['maydon']}, aholisi {malumot['aholi']},"
          f" valyutasi {malumot['pul birligi']}")
