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
