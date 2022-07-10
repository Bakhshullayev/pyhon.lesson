# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

yangi_mahsulot = []

while True:
    mahsulot = (input('Mahsulot nomini kiriting'))
    yangi_mahsulot.append(mahsulot)
    javob = input('Yana mahsulot qo\'shasizmi ha/yoq')

    if javob != 'ha':
        break

print(yangi_mahsulot)

# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

e_bozor = {}

while True:
    mahsulot = input('Mahsulot nomini kiriting')
    narx = input(f'{mahsulot.title()} narxini kirinting')
    e_bozor[mahsulot] = narx
    javob = input('yana mahsullot qo\'shasizmi  ha/yoq')
    if javob != 'ha':
        break

# Yuqoridagi ikki dasturni jamlaymiz.
# Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring' \
# (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring,
# aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating

buyurtmalar = ['olma', 'anjir', 'uzum', 'qovun']
mahsulotlar = {'olma': 20000,
               'shaftoli': 25000,
               'tarvuz': 18000,
               'uzum': 22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
