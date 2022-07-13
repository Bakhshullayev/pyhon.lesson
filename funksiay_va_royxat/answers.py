# Matnlardan iborat ro'yxat qabul qilib,
# ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.

def katta_harf(matnlar):
    matnlar = matnlar[:]
    for harf in range(len(matnlar)):
        matnlar[harf]=matnlar[harf].title()
    return matnlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)

# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan
# va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.
