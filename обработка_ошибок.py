# обработка ошибки деления на ноль
b = 0
a = 5
try:
    x = a/b
    print(x)
except ZeroDivisionError:
    print("К сожалению произошло деление на ноль...")
input("Click enter for continue...")
# ввод "да" или "нет" с поправкой на корректное значение
response = None
while response != "y" and response != "n" and response != "Y" and response != "N":
    response = input("Введите 'Y' или 'N': ")
    if response == "y" or response == "n" or response == "Y" or response == "N":
        break
    else:
        print("Введите корректное значение...")

input("Нажмите Enter для завершения программы...")
