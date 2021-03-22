text_file = open("1.txt", "r", encoding='utf-8')
for line in text_file:
    print(line, end="\n")
print(text_file.readline())
text_file.close()

