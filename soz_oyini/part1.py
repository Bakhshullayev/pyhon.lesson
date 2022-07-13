from random import randint

x = randint(0, 11)
urinish = 0
while True:
    urinish +=1
    y = int(input('son kirit >> '))
    if y == x:
        print('topdingiz')
        print(f"Siz {urinish} ta topdingiz")
        break
    if y < x:
        print("men o'ylagan son bundan katta")
    if y > x:
        print("men o'ylagan son bundan kichik")



