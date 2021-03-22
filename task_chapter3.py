#Игра кости
#Вызов модуля random
import random
first_side = random.randint(1, 6)
second_side = random.randrange(1, 6) + 1
total = first_side + second_side
print("Сделайте ваш первый ход:", first_side)
input("Нажмите Enter для продолжения...")
print("Сделайте ваш второй ход:", second_side)
input("Нажмите Enter для подсчёта общего числа очков...")
print("Ваша сумма составила:",total)
if total <= 10:
    print("Подздравляем, вы выиграли!")
else:
    print("К сожалению, вы проиграли...")

