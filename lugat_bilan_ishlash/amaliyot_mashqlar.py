# otam (onam, akam, ukam, va hokazo) degan lug'at yarating
# va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo).
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

dadam = {'ism': "Sadullo",
         'yosh': '1976',
         'tumani': 'Romitan',
         'manzili': 'Buxoro'
         }
print(
    f"Otamning ismlari {dadam['ism']}, {dadam['yosh']} - yilda, {dadam['manzili']} viloyatining {dadam['tumani']} tumanida tug'ilganlar")

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing.
# Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring:
# misol uchun : Alining sevimli taomi osh

ovqatlar = {
    'otam': 'osh',
    'onam': 'norin',
    'ukam': 'qozon kabob',
    'men': 'sho\'rva'

}
print(f"Dadamning sevimli ovqatlari {ovqatlar['otam']}")
print(f"Onamning  sevimli ovqatlari {ovqatlar['onam']}")
print(f"Ukamning sevimli ovqati {ovqatlar['ukam']}")
print(f"Mening sevimli ovqatim {ovqatlar['men']}")

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

python_org = {
    'integer': 'butun son',
    'float': 'o\'nlik son',
    'string': 'matn',
    'get()': 'yangi qiymat qo\'shish ',
    '.len()': 'qiymatni uzunligini aniqlash'

}
print(f"Integer deganda {python_org['integer']} tushuniladi, float deganda {python_org['float']} tushuniladi"
      f" .get metodi esa {python_org['get()']}tushuniladi")

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

translator = {
    'apple':'olma',
    'banana':'banan'
}
word = input('So\'z kiriting')
print(translator.get(word,"Bunday so'z mavjud emas"))






