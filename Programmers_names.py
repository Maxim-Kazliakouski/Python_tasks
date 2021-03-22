num = 0
while num != 1001:
    num = int(input("Введите новое число программистов: "))
    if (num % 10 == 0) or (5 <= num % 10 <= 9) \
            or num == 11 or num == 12 or num == 13 or num == 14 \
            or num % 100 == 11 or num % 100 == 12 or num % 100 == 13 or num % 100 == 14:
        print(num, "программистов")
    elif 2 <= num % 10 <= 4:
        print(num, "программиста")
    elif num % 10 == 1:
        print(num, "программист")
        if num == 1001:
            print("Вы ввели максимальное количество программистов!")