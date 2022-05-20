def kalc(a, b, num):
    if (num == 1):
        rez = a + b
        print(str(a) + " + " + str(b) + " = " + str(a+b))
    if (num == 2):
        print("Результат: " + str(a - b))
    if (num == 3):
        print("Результат: " + str(a * b))
    if (num == 4):
        print("Результат: " + str(a / b))
    if (num == 5):
        print("Результат: " + str(math.ceil(a/b)))
    if (num == 6):
        print("Выберите число, которое хотите возвести в корень: "
              "\n 1. " + str(a) + "\n 2. " + str(b))
        o = int(input())
        if (o == 1):
            print("Результат: " + str(math.sqrt(a)))
        else:
            print("Результат: " + str(math.sqrt(b)))
    if (num == 7):
        print("Результат: " + str(math.fmod(a, b)))
    if (num == 8):
        print("Введите ещё одну переменную для подсчёта площади: ")
        c = float(input())
        Area = {
            'Per': (lambda a, b: 2*(a + b)),
            'Plo': (lambda a, b, c: 2*(a * b + b * c + a * c)),
        }
        print('Периметр = ', Area['Per'](a, b))
        print('Площадь = ', Area['Plo'](a, b, c))
    if (num == 9):
        if(a < 0):
            print("\n Введены числа меньше нуля. Числа были возведены в модуль!!! \n")
        if(b < 0):
            print("\n Введены числа меньше нуля. Числа были возведены в модуль!!! \n")
        proc = b * 100 / a
        print("Процент от числа " + str(math.fabs(a)) + " равен " + str(math.fabs(proc)) + " %")
    if (num == 10):
        print("Результат: " + str(pow(a, b)))
    if (num == 11):
        print("Выберите число: " "\n 1. " + str(a) + "\n 2. " + str(b))
        o = int(input())
        if (o == 1):
            print("Ответ: " + str(math.log10(a)))
        if (o == 2):
            print("Ответ: " + str(math.log10(b)))
    if (num == 12):
        print("Выберите число: " "\n 1. " + str(a) + "\n 2. " + str(b))
        o = int(input())
        if (o == 1):
            print("Ответ: " + str(math.sin(a)))
        if (o == 2):
            print("Ответ: " + str(math.sin(b)))