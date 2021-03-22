"""
#   подсчёт количества букв "С" в троке
word = "CACCTGGAC"
quan = 0
for n in word:
    if n == "C":
        quan += 1
print("Results:", quan)

# БЫСТРЫЙ подсчёт количества букв "С" в строке
word = "CACCTGGAC"
print(word.count("C"))

#   подсчёт нескольких символов в незавимости от регистра
word = input()
n1 = 0
n2 = 0
for n in word:
    if n == "g" or n == "G":
        n1 += 1
    elif n == "c" or n == "C":
        n2 += 1
print("Count C and c = ", n2)
print("Count G and g = ", n1)
e = len(word)
print(e)
print(((n1 + n2) / e) * 100)
#   второй способ
word = "CGacggtgttat"
a = word.count("C")
b = word.count("c")
c = word.count("G")
d = word.count("g")
e = len(word)
print(((a+b+c+d)/e)*100)
"""
# проверка на то, читается ли строка с право налево и наоборот одинаково
word1 = "acqwdwqbbca"
i = 0
j = len(word1)-1
polindrom = True
while i < j:
    if word1[i] != word1[j]:
        polindrom = False
        i += 1
        j -= 1
if polindrom:
    print("YES")
else:
    print("NO")
