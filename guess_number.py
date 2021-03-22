# подсоединение модуля
import random
name = input("Привет! Введи своё имя: ")
print("Привет", name + "!")
print("За сколько попыток вы угадаете число,", name + "?", end="")
#   количество попыток
popitki = input(" Напишите своё предположение в цифрах: ")
# количество попыток
atemptions = int(popitki)
# количество попыток для вывода после цикла
attempt = 1
# корректное отображение спряжений слова "попытка"
if atemptions % 10 == 0 or 5 <= atemptions % 10 <= 9 \
        or atemptions == 11 or atemptions == 12 or atemptions == 13 or atemptions == 14 \
        or atemptions % 100 == 11 or atemptions % 100 == 12 or atemptions % 100 == 13 or atemptions % 100 == 14:
    print("У Вас есть", atemptions, "попыток!")
elif 2 <= atemptions % 10 <= 4:
    print("У Вас есть", atemptions, "попытки!")
elif atemptions % 10 == 1:
    print("У Вас есть", atemptions, "попытка!")
# обозначение переменной
chislo = 0
a = random.randint(1, 100)
while chislo != a:
    chislo = int(input("Введите число: "))
    if chislo != a:
        print("Не угадали...")
        if atemptions <= 1:
            print("К сожалению вы не угадали...")
            break
        #    наращивание попыток
        attempt += 1
        atemptions -= 1
    #    сравнение числа с загаданным
    if chislo > a:
        print("Данное число больше загаданного...введите меньшее число и попробуйте еще раз!")
    #    сравнение числа с загаданным
    elif chislo < a:
        print("Данное число меньше загаданного...введите большее число и попробуйте ещё раз")
    else:
        print("Поздравляем,", name + ",", "Вы угадали число с", attempt, "попытки!")
input("Нажмите Enter для выхода из программы...")