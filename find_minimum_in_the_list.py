spisok = [5, 8, 4, 3, 5, 7, 1, 0, 25, 46]
# задаём переменную, которую будем сравнивать изначально
m = spisok[0]
# задаём цикл, где мы перебираем все значения нашего списка
for x in spisok:
    # сравниваем наше первое значение с переменной "m"
    if m > x:
        # если переменная m > x тогда мы перезаписываем переменную, т.е. если 4 > 3, тогда мы записываем 3 и т.д.
        x = m
print(m)