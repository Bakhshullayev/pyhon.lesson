def func1(ism, date):
    """ismi va yoshini chiqaruvchi funksiya """
    return f'{ism.title()} {2022 - date}yoshda'


def func2(num):
    """soning kvadrati va kubini hisoblovchi funksiya"""
    return f"Kvadrati: {num ** 2}, Kubi: {num ** 3}"


def func3(num):
    """sonning juft yoki toqligini aniqlovchi dastur"""
    if num % 2:
        return f"{num} soni Toq"
    return f"{num} soni Juft"


def func4(num1, num2):
    """soning kattasini aniqlovchi funksiya"""
    if num1 > num2:
        return f"{num1} > {num2}"
    if num1 < num2:
        return "{} < {}".format(num1, num2)
    return "{son1} = {son2}".format(son2=num2, son1=num1)


def func5(4x, y=2):
    """sonlarni x va y ning kvadaratini aniqlovchi funksiya"""
    return f'{x ** y}'


def func6(x):
    """soning 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linmasi"""
    for son in range(2, 11):
        if x % son == 0:
            print(f'{x}ga {son} qoldiqsiz bo\'linadi')


func6(70)
