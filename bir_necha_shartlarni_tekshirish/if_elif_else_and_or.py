# # Foydalanuvchidan juft son kiritishni so'rang.
# # Agar foydalanuvchi juft son kiritsa "Rahmat!",
# # agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
#
juft_son = int(input('Juft son kiriting'))
if juft_son % 2:
    print('Juft son kiriting')
else:
    print("Rahmat")
#
# # Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# # Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# # Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# # Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
#
yosh = int(input('Yoshingizni kiriting'))
if yosh < 4 or yosh > 60:
    summa = "bepul"
elif yosh < 18:
    summa = 10000
elif yosh > 18:
    summa = 20000

print(f'Muzeyimizga kirish uchun sizga', summa, 'bo\'ladi')
#
# # Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va
# # ularning teng yoki katta/kichikligi haqida xabarni chiqaring
#
x = int(input(" Birinchi sonni kiriting"))
y = int(input(" Ikkinchi sonni kiriting"))
if x == y:
    print(f'{x} = {y}')
elif x < y:
    print((f'{x} < {y}'))
elif x > y:
    print((f'{x} > {y}'))
#
# # Yuqoridagi dasturni quyidagicha o'zgartiring:
# # foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
# # Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi, bor_mahsulotlar degan ro'yxatga,
# # do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.
# # Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni,
# # aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
#
mahsulotlar = ['anor', 'anjir', 'banan', 'olma', 'nok']

bor_mahsulotlar = []
mavjud_emas = []

for _ in range(5):
    mahsulot = input("Kirit -> ")
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if len(mavjud_emas) == 0:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
else:
    print("Do'konimizda quyidagi mahsulotlar yo'q: {}".format(mavjud_emas))

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing.
# Foydalanuvchidan yangi login tanlashni so'rang
# va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!"
# aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

foydalanuvchilar = ["anvar", 'shox', 'sardor', 'nozim']
yangi_login = input('yangi login tanlang')
if yangi_login in foydalanuvchilar:
    print("Login band yangi login tanlang")
else:
    print(f'Xush kelibsiz\'{yangi_login.title()}')

# Foydalanuvchidan biror butun son kiritishni so'rang.
# Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

foydalanuvchi = float(input("Butun son kiriting"))
for x in range(2, 11):
    if not (foydalanuvchi % x):
        print(f'{foydalanuvchi}soni {x} ga qoldiqsiz bo\'linadi')
