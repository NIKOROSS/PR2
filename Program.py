import os
import math

clear = lambda: os.system('cls')
rez = 0

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

def stroka(s):
    clear()
    print("Строка - " + str(s))
    print("Длина введённой строки = " + str(len(s)))
    print("Число пробелов = " + str(s.count(' ')))
    print("Число запятых = " + str(s.count(',')))



while True:
    print("Выберите нужный вариант:"
          "\n 1. Калькулятор"
          "\n 2. Подсчет в строке"
          "\n 3. Матрица"
          "\n 0. Выход")
    try:
        variant = int(input())
        if (variant == 1):
            while True:
                clear()
                print("Выберите функцию:"
                      "\n 1. Обычный калькулятор"
                      "\n 0. Назад")
                kal = int(input())
                if (kal == 0):
                    clear()
                    break
                if (kal == 1):
                    print("Введите числа: \n")
                    a = float(input())
                    b = float(input())
                    while True:
                        print("\n Выберите действие:"
                              "\n 1. Сложение"
                              "\n 2. Вычитание"
                              "\n 3. Умножение"
                              "\n 4. Деление"
                              "\n 5. Деление нацело"
                              "\n 6. Корень"
                              "\n 7. Нахождение остатка после деления"
                              "\n 8. Площадь и периметр параллелепипеда"
                              "\n 9. Процент от числа a"
                              "\n 10. Степень"
                              "\n 11. Логарифтм по основанию 10"
                              "\n 12. Синус"
                              "\n 0. Назад")
                        num = int(input())
                        kalc(a, b, num)
                        if (num == 0):
                            clear()
                            break
        elif (variant == 0):
            print("Завершение работы!")
            break
        elif (variant == 2):
            print("Заполните строку: ")
            s = str(input())
            if(s != ""):    
                stroka(s)
        elif (variant == 3):
            print("Введите количество строк: ")
            N = int(input())
            print("Введите количество столбцов: ")
            M = int(input())
            A = []
            for i in range(N):
                A.append([0] * M)
            print("Введите первое число: ")
            g = int(input())
            print("Введите увеличитель: ")
            c = int(input())
            for i in range(N):
                for j in range(M):
                    A[i][j] = g
                    g += c

            for i in range(len(A)):
                for j in range(len(A[i])):
                    print(A[i][j], end=' ')
                print()
            print("Матрица имеет " + str(N) + " строк и " + str(M) + " столбцов \n" )
    except:
        clear()
        print("Данные введены не корректно!!!")
