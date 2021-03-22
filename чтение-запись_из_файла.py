"""text_file = open("1.txt", "r", encoding='utf-8')
for line in text_file:
    print(line, end="\n")
#print(text_file.readline())
text_file.close()

text_file = open("2.txt", "r", encoding='utf-8')
read_file = text_file.read()
print(read_file)
text_file.close()
"""
text_file = open("Questions for repeating.txt", "w", encoding='utf-8')
write_in_file = text_file.write("1) Повторить виды тестирования" "\n"
                                "2) It's me, Max" "\n"
                                )
text_file.close()