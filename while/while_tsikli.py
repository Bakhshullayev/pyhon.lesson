# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
# Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating

kitob = ('Yaxshi ko\'rgan kitoblaringizni kiriting,')
kitob += 'dasturni tugatmoqchi bo\'lsangiz "stop"deb yozing'
while True:
    savol = input(kitob)
    if savol == "stop":
        break
print('dastur tugadi')

# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq:
# 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul.
# Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
# Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

yosh = 'Yoshingizni kiriting'

while True:
    savol = input(yosh)

    if savol == 'exit' or savol == 'stop':
        break
    qiymat = int(savol)

    if qiymat < 7:
        summa = 2000
    elif 7 < qiymat < 18:
        summa = 3000
    elif 18 < qiymat < 65:
        summa = 10000
    else:
        summa = 'bepul'

    if summa == 'bepul':
        print('sizga bepul')
    else:
        print(f'chipta narhi {summa} so\'m')

# Quyidagi dasturda bir nechta mantiqiy xatolar bor.
# Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?

savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)

    if qiymat == 'exit':
        break
    elif float(qiymat) < 0:
        continue
    else:
        ildiz = float(qiymat) ** (0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
