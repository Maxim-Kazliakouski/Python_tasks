"""
# создание пустого кортежа
inventory = ()
if not inventory:
    input("There is nothing..." "\n" "please click 'Enter' to continue")
# создание полного кортежа:
inventory = ("меч",
             "щит",
             "кольчуга",
             "шлем",
             "доспехи")
print("Вот что имеется в наличии:")
for item in inventory:
    print(item)
things = len(inventory)
print("Количество предметов:", things)
index = int(input("Выберете номер предмета: "))
print("Под данным номером находится:", inventory[index])
"""

# подключение модуля random
import random

# создание кортежа, из которого будут выбираться слова
WORDS = ("программирование",
         "питон",
         "время",
         "конкатенация",
         "отдых")
# выбор случайного слова из кортежа WORDS при помощи функции random.choice()
word = random.choice(WORDS)
# print(word)
# создаём переменную для конечного сравнения с выбранным словом
correct = word
# переменная для нового слова с перепутанными буквами
jumble = ""
# задаём количество попыток
atemptions = 2

while word:
    # выбираем случайный индекс буквы из выбранного слова
    position = random.randrange(len(word))
    # добавляем эту букву в переменную jumble
    jumble += word[position]
    #print(jumble)
    # записываем условие когда цикл прервётся, т.е. когда слово закончится -> тогда и цикл оборвётся
    word = word[:position] + word[(position + 1):]
print("Раставьте буквы слова ->", jumble, end=" ")
print("в правильном порядке.")
if atemptions % 10 == 0 or 5 <= atemptions % 10 <= 9 \
        or atemptions == 11 or atemptions == 12 or atemptions == 13 or atemptions == 14 \
        or atemptions % 100 == 11 or atemptions % 100 == 12 or atemptions % 100 == 13 or atemptions % 100 == 14:
    print("У Вас есть", atemptions, "попыток!", end="")
elif 2 <= atemptions % 10 <= 4:
    print("У Вас есть", atemptions, "попытки!", end="")
elif atemptions % 10 == 1:
    print("У Вас есть", atemptions, "попытка!", end="")
slovo = input("\n" "Запишите свой ответ ниже: " "\n")
# задаём условие для попыток отгадывания
while slovo != correct:
    slovo = input("Попробуйте ещё раз..." "\n")
    atemptions += 1
    if atemptions > 2:
        print("К сожалению вы не угадали. Количество попыток исчерпано.")
        break
    elif slovo == correct:
        print("Поздравляем, вы угадали данное слово." "\n" "Это было слово -->", correct + "!")
