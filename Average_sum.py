a, b = input().split()
a = int(a)
b = int(b)
s = 0
# счётчик для количество чисел, кратных 3
q = 0
for i in range(a, b+1):
    if int(i) % 3 == 0:
        # сумма чисел кратных 3
        s = i + s
        # запись количества чисел
        q += 1
        print(i)
print(s/q)
