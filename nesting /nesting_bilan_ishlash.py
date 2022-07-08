# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang.
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

vohidov = {'ism': 'Erkin Vohidov',
           'tyil': 1936,
           'vyil': 2016,
           'tjoy': "Farg'ona",
           'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
           }


navoiy = {'ism': 'Alisher Navoiy',
          'tyil': 1441,
          'vyil': 1501,
          'tjoy': "Xirot",
          'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
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
