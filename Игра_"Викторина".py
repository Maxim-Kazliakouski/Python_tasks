def title():
    text_file = open("quiz.txt", "r", encoding='utf-8')
    read_file = text_file.readline()
    return read_file


def welcome():
    return print("Добро пожаловать в игру -", title())


def next_line():
    line = read_file