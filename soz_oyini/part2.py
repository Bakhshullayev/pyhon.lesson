from random import randint

son = randint(1, 10)
left = 0
right = 10

urinish = 0

while True:
    urinish += 1
    x = input(f"Men o'ylagan son {son}, agar to'g'ri bo'lsa [T], katta bo'lsa [+], kichik bo'lsa [-] kiriting >> ")
    if x == 'T':
        print("Bratishka men topdim 😎")
        print(f"Bratishka men {urinish}ta urinishda topdim")
        break

    if x == "+":
        left = son + 1
        son = (left + right) // 2

    if x == "-":
        right = son - 1
        son = (left + right) // 2
