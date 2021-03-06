# Ввод числа, в котором цифры не повторяются. Поиск возможных комбинаций. Поиск макс комбинации.
import time  # чисто что бы было, на моем ноутпуке 1234567890 считается за ~200 сек
# Загадка от Жака Фреско - если есть "from itertools import *", то зачем весь код снизу??
# На ответ - две функции


# Функция по принципу дерева перебирает все возможные комбинации
# (берется цифра => строятся все её вариации с другими цифрами из списка, но не включая уже имеющиеся цифры =>
# то же самое повторяется для новых построенных значений,
# до тех пор, пока длинна построенной строки не совпадет с длинной списка цифр =>
# PROFFIT

def Derevo_variantov(n):  # n - первая цифра в списке
    if len(n) == len(List):
        print(n)
    for i in range(len(List)):
        x = n
        if List[i] not in x:
            x += List[i]
            Derevo_variantov(x)


def Sovpadenie(M):  # Проверка на совподения цифр в комбинации
    for i in range(11):
        if M.count(str(i)) > 1:
            return True


print("Для выхода из программы введите число - 404")
while True:  # Кручусь в цикле просто потому что могу :^)
    try:
        Vvod = int(input("Введите целое число, цифры которого не повторяются: "))  # Ввод числа
        if Vvod == 404:
            break
        start_time = time.time()
        if Vvod < 0:  # Проверка на отрицательность
            Vvod *= -1
        Vvod = str(Vvod)  # Работаем со строкой
        List = []
        biggest = ""
        for i in range(len(Vvod)):  # Заполнение списка цифрами для комбинации
            List.append(Vvod[i])
        if not Sovpadenie(List):  # Проверка на совпадения цифр в числе
            for i in range(len(List)):  # Поочерердно закидываем элементы в функцию и исключаем 0
                if List[i] != '0':  # C нуля цифры не начинаются - Да ладно?)
                    Derevo_variantov(List[i])
            List.sort()
            for i in range(len(List)):  # Составление наименьшей строки (потом перевернём)
                biggest += List[i]
            print("Наибольшая комбинация:", biggest[::-1])  # Переворачиваем
            print("--- %s seconds ---" % (time.time() - start_time))
        else:
            print()
            print("///Цифры в числе не должны повторяться///")
    except ValueError:
        print()
        print("///Введите целое число///")
