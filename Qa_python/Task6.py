# ----- Task 1 -----
# найти сумму массива
arr = [9, 2, 6, 4, 5, 12, 7, 8, 6]
summa = 0
for each_elem in arr:
    summa += each_elem
print(summa)
# min_elem = min(arr)
# max_elem = max(arr)
# print(max_elem, min_elem)

# ----- Task2 ----
# найти максимальное значение массива
arr = [9, 2, 6, 4, 5, 12, 7, 8, 6]
# допускаем, что максимальное занчение в массиве arr это элемент с индексом 0
max_elem = arr[0]
l = len(arr)
for each_elem in range(1, l):
    if arr[each_elem] > max_elem:
        max_elem = arr[each_elem]
print(max_elem)

# ----- Task3 ----
# найти максимальое значение массива
arr = [9, 2, 6, 4, 5, 12, 7, 8, 6]
# допускаем, что минимальное занчение в массиве arr это элемент с индексом 0
min_elem = arr[0]
l = len(arr)
for each_elem in range(1, l):
    if arr[each_elem] < min_elem:
        min_elem = arr[each_elem]
print(min_elem)

# ---- Task 4 -----
# вывод среднеарифмитического массива
arr = [9, 2, 6, 4, 5, 12, 7, 8, 6]
summa = int()
sred_arif = int(summa / l)
l = int(len(arr))
for each_elem in arr:
    summa += each_elem

sred_arif = int(summa / l)
print(sred_arif)

# ---- Task 5 ----
# вывести сумму значений массива
arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9], [-1, -2, -3, -4], [-5, -6]]
suma = 0
for pod_elem in arr:
    suma += sum(pod_elem)
print(suma)

# ---- Task 6 -----
# вывести максимальное знаение массива
arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9], [-1, -2, -3, -4], [-5, -6]]
max_elem = arr[0]

l = len(arr)
for each_elem in range(1, l):
    if arr[each_elem] > max_elem:
        max_elem = arr[each_elem]

a = list(max_elem)
max_elem = a[0]
l_a = len(a)
for each_elem in range(0, l_a):
    if a[each_elem] > max_elem:
        max_elem = a[each_elem]
print(max_elem)

# ---- Task 7 ----
# Необходимо вывести количество элементов в каждом из подмассивов
arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9], [-1, -2, -3, -4], [-5, -6]]
i = 0
for element in arr:
    i += len(arr)
print(i)

# ---- Task 8 -----
# необходимо подсчитать количество строк в массиве, которые не содержат буквы “е”
arr = [['Привет', 'всем', 'кто'], ['изучает', 'язык', 'программирования']]
kol_str = []
for pod_arr in arr:
    for slovo in pod_arr:
        if 'е' not in slovo:
            kol_str.append(slovo)
print('The amount of strings, that do not contain letter "e" =', len(kol_str))
