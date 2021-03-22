def question_yes_no():
    response = None
    while response != 'y' and response != 'n':
        response = input("Введите 'y' или 'n':")
    return response


answer = question_yes_no()
print("Вы вели", answer)


