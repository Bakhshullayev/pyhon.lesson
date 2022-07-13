from random import randint


def func1():
    x = randint(0, 10)

    urinish = 0

    while True:
        urinish += 1
        y = int(input('son kirit >> '))
        if y == x:
            print('topdingiz')
            break
        if y < x:
            print("men o'ylagan son bundan katta")
        if y > x:
            print("men o'ylagan son bundan kichik")
    return urinish


def func2():
    son = randint(1, 10)
    left = 0
    right = 10

    urinish = 0

    while True:
        urinish += 1
        x = input(f"Men o'ylagan son {son}, agar to'g'ri bo'lsa [T], katta bo'lsa [+], kichik bo'lsa [-] kiriting >> ")
        if x == 'T':
            break

        if x == "+":
            left = son + 1
            son = (left + right) // 2

        if x == "-":
            right = son - 1
            son = (left + right) // 2
    return urinish


def main():
    print("So'z topish o'yini")

    while True:
        javob = input("O'ynaymizmi yes/no >> ")

        if javob == 'no':
            break

        print("Men son o'yladim siz toping")
        ur_1 = func1()

        print("Siz o'ylang men topaman")
        ur_2 = func2()

        if ur_1 < ur_2:
            print(f"Siz {ur_1} ta urinishda men esa {ur_2} ta urinishda topdim va qoldim!")
        elif ur_2 == ur_1:
            print("Durang")
        else:
            print(f"Siz {ur_1} ta urinishda men esa {ur_2} ta urinishda topdim va yutdim!")


if __name__ == '__main__':
    main()
