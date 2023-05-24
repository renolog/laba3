def r1():
    n = int(input())
    str = ''

    for i in range(1, n + 1):
        sl = input()
        str = str + sl + ' '
        sl = ''

    print(str)


def r2():
    str = ''
    sl = input()

    while sl != 'stop':
        str = str + sl + ' '
        sl = input()
    print(str)

def r3():
    sl = input()
    letter1 = 'ф'
    letter2 = 'Ф'

    while sl!= 'stop':
        if (letter1 in sl) or (letter2 in sl):
            print("Это редкое слово")
        else:
            print("Это не редкое слово.")
        sl = input()

def r4():
    import random
    n = 0
    v = 0
    while n != 3:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        res = a + b
        otvet = input(str(a) + "+" + str(b) + "= ")

        if otvet == str(res):
            print("Верно")
            v += 1
        else:
            print("Ответ неверный")
            n += 1
    print("Количество правильных ответов: ", v)

r4()