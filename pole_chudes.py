# подключение модуля random
import random
# создание кортежа, из которого будут выбираться слова
WORDS = ("программирование",
         "автомобиль",
         "компьютер",
         "телефон",
         "понедельник")
# выбор случайного слова при попмощи функции random.choice
word = random.choice(WORDS)
# присвоение случайно выбранного слова переменной correct
correct = word
# определение количества символов в случайно выбранном слове
word_length = len(word)
# подключение модуля с правильным спряжением слов
if word_length % 10 == 0 or 5 <= word_length % 10 <= 9 \
        or word_length == 11 or word_length == 12 or word_length == 13 or word_length == 14 \
        or word_length % 100 == 11 or word_length % 100 == 12 or word_length % 100 == 13 or word_length % 100 == 14:
    print("Необходимо угадать слово, которое состоит из", word_length, "букв!", end="")
elif 2 <= word_length % 10 <= 4:
    print("Необходимо угадать слово, которое состоит из", word_length, "букв!", end="")
elif word_length % 10 == 1:
    print("Необходимо угадать слово, которое состоит из", word_length, "буквы!", end="")
print("\n" "Вы можете попробовать отгадать любые 5 букв!")
input("Если вы готовы, нажмите кнопку 'Enter'!")
# создание переменной, куда будут записываться угаданные буквы из случайно выбранного слова
guess_symbols = ""
n = input("Введите первую букву: ")
if n in word:
    guess_symbols += n + " "
n = input("Введите вторую букву: ")
if n in word:
    guess_symbols += n + " "
n = input("Введите третью букву: ")
if n in word:
    guess_symbols += n + " "
n = input("Введите четвёртую букву: ")
if n in word:
    guess_symbols += n + " "
n = input("Введите пятую букву: ")
if n in word:
    guess_symbols += n + " "
print("Вот буквы, которые есть в этом слове:", guess_symbols.upper())
print("Теперь попробуйте отгадать слово целиком!")
user_word = input("Введите слово: ")
# количество попыток для угадывания
guess = 5
# создание цикла для 5 попыток
while user_word != correct:
    if guess % 10 == 0 or 5 <= guess % 10 <= 9 \
            or guess == 11 or guess == 12 or guess == 13 or guess == 14 \
            or guess % 100 == 11 or guess % 100 == 12 or guess % 100 == 13 or guess % 100 == 14:
        print("Попробуйте ещё раз! У Вас осталось", guess, "попыток!", end="")
        guess -= 1
        user_word = input("\n" "Ведите слово снова: ")
    elif 2 <= guess % 10 <= 4:
        print("Попробуйте ещё раз! У Вас осталось", guess, "попытки!", end="")
        guess -= 1
        user_word = input("\n" "Ведите слово снова: ")
    elif guess % 10 == 1:
        print("Попробуйте ещё раз! У Вас осталось", guess, "попытка!", end="")
        guess -= 1
        user_word = input("\n" "Ведите слово снова: ")
    if guess == 0:
        print("К сожалению количество попыток исчерпано...")
        break
if user_word == correct:
    print("Поздравляем, Вы отгадали слово!" "\n" "Это было слово", correct.upper() + "!")