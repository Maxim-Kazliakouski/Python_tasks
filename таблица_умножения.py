# для того, чтобы вывести таблицу с перемноженными числами
# изначально необходимо вывести две строки, а затем уже перемножать данные строки
a = int(input())
b = int(input())
c = int(input())
d = int(input())
# выводим шапку таблицы
for i in range(c, d + 1):
    print("\t", i, end="")
print(end="\n")
# заполнение первой строки при первом проходе цикла for
for g in range(a, b + 1):
    print(g, "\t", end="")
    for n in range(c, d + 1):
        print(g*n, end="\t")
    print(end='\n')