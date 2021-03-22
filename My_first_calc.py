a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Введите операцию: ")
vibor = operation
#sum = "+"
#sub = "-"
#div = "/"
#mul = "*"
#od = "%"
#pow = "**"
if vibor == "+":
    print("Результат", a+b)
elif vibor == "-":
    print("Результат", a-b)
elif vibor == "*":
    print("Результат", a * b)
elif vibor == "pow":
    print("Результат", a ** b)
elif vibor == "div" and b != 0:
    print("Результат", a // b)
elif vibor == "mod" and b != 0:
    print("Результат", a % b)
elif vibor == "/" and b != 0:
    print("Результат", a / b)
else:
    print("Деление на 0!")