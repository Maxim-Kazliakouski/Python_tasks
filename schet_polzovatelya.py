""""
nachalo = int(input("Введите начало интервала: "))
konec = int(input("Введите конец интервала: "))
shag = int(input("Введите шаг: "))
schet = range(nachalo, konec, shag)
print("Вот весь диапазон чисел: ")
for i in schet:
    print(i, end=" ")

word = input()
naoborot = word[::-1]
print("Слово наоборот:", naoborot)

word = "программирование"
a = len(word)
for i in word:
    print(i.upper(), end=" ")
print("\n", a)


# программа для суммирования крайних чисел:
s = [1, 3, 5, 6, 10]
t = []
l = len(s)-1
k = 0
i = 0
if len(s)==0:
    print(str(0))
else:
    for st in s:
        if len(s)>1:
            if i==0:
                k = s[i+1] + s[-1]
                t.append(k)
            elif i>0 and i<l:
                k=s[i-1]+s[i+1]
                t.append(k)
            elif i==l:
                k = s[i-1]+s[0]
                t.append(k)
        elif len(s)==1:
            k = s[i]
            t.append(k)
        i +=1
    j = 0
    for st2 in t:
        print(str(t[j])+' ',end='')
        j +=1
"""
# программа для вывода повторяющихся значений
s = [4, 8, 0, 3, 4, 2, 0, 3]
t = []
s.sort()
l = len(s) - 1
if len(s) != 1:
    for i in range(0, l):
        if s[i] == s[i + 1]:
            t.append(s[i])
    for j in range(l, l + 1):
        if s[-1] == s[-2]:
            t.append(s[j])
n = len(t)
for g in range(0, n):
    print(t[g], end=' ')
