# В данной задаче идёт сравненеие первых 3-х цифр и последних 3 цифр
ticket = int(input())
a = ticket % 1000
a1 = a % 10
pr1 = a // 10
a2 = pr1 % 10
a3 = a // 100
sec = ticket // 1000
b1 = sec % 10
pr2 = sec // 10
b2 = pr2 % 10
b3 = sec // 100
if (a1 + a2 + a3) == (b1 + b2 + b3):
    print("Счастливый")
else:
    print("Обычный")
