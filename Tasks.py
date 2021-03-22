"""a=int(input())
x=a/4
y=a/100
z=a/400
if a%4==0 and y>0 and a%400==0:
    print("Високосный")
else:
    print("Обычный")

a = int(input())
b = int(input())
c = int(input())
s = (((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))**0.5
print(float(s))

a = int(input())
if (-15 < a <= 12) or (14 < a < 17) or (a >= 19):
    print("True")
else:
    print("False")

# программа для вывода максимального и минимального числа

a = int(input())
b = int(input())
c = int(input())
s = a + b + c;
print(max(a,b,c))
print(min(a,b,c))
print(s - max(a,b,c) - min(a,b,c))

# программа для суммы вводимых чисел до тех пор, пока не будет введён 0
a = int(input())
s = 0
while a != 0:
    s += a
    a = int(input())
else:
    print(s)

# нахождение общего знаменателя
a = int(input())
b = int(input())
d = 1
while d % a != 0 or d % b != 0:
    d += 1
else:
    print(d)
 # кусок кода...
    while i < 10:
    b = int(input())
    if b < 10:
        break
    if b > 100:
        break
    if 10 <= b <= 100:
        print("B = ", b)
        break
i += 1
while i < 10:
    c = int(input())
    if c < 10:
        break
    if c > 100:
        break
    if 10 <= c <= 100:
        print("C = ", c)
        break
i += 1
while i < 10:
    d = int(input())
    if d < 10:
        break
    if d > 100:
        break
    if 10 <= d <= 100:
        print("D = ", d)
        break
i += 1
while i < 10:
    e = int(input())
    if e < 10:
        break
    if e > 100:
        break
    if 10 <= e <= 100:
        print("E = ", e)
        break
i += 1
    """
i = 0
while i < 1:
    a = int(input())
    if a < 10:
        continue
    elif a > 100:
        break
    else:
        print("A = ", a)
        i += 1
        i1 = 0
        while i1 < 1:
            b = int(input())
            if b < 10:
                continue
            elif b > 100:
                break
            else:
                print("B = ", b)
                i1 += 1
                i2 = 0
                while i2 < 1:
                    c = int(input())
                    if c < 10:
                        continue
                    elif c > 100:
                        break
                    else:
                        print("C = ", c)
                        i2 += 1
                        i3 = 0
                        while i3 < 1:
                            c = int(input())
                            if c < 10:
                                continue
                            elif c > 100:
                                break
                            else:
                                print("C = ", c)
                                i3 += 1
                                i4 = 0
                                while i4 < 1:
                                    e = int(input())
                                    if e < 10:
                                        continue
                                    elif e > 100:
                                        break
                                    else:
                                        print("E = ", e)
                                        i4 += 1
                                        break