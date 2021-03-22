# создание списка с кортежами внутри
records = [(1000, "Kris"), (3000, "Andrew"), (2000, "Max")]
# присвоение переменной нулевого значения
choice = None
# создание цикла для отображения меню
while choice != 0:
    print("\n" "Records")
    print("0 - Exit" "\n" "1 - Show the records" "\n" "2 - Add the records")
    choice = int(input("Your choice: "))
    if choice == 1:
        print("Records" "\n" "Result" "\t" "Name")
        # задание сортировки путём ввода функции .sort (в данном случае стоит от max к min)
        records.sort(reverse=True)
        # ограничение выводимого списка до 5
        records = records[:5]
        for entry in records:
            # разбивка данных на двое, т.е. отдельно отображаются данные под переменной score и name
            score, name = entry
            print(score, "\t", name)
        input("Press 'Enter' button to relocate to main menu...")
    elif choice == 2:
        print("Please, input the record in next order:" "\n" " - 'name'" "\n" " - 'score'")
        score = int(input("Please, input the SCORE: "))
        name = input("Please, input the NAME of recordsman: ")
        # в каком формате будет добавлен кортеж в список
        entry = (score, name)
        # добавление кортежа в конец списка
        records.append(entry)
    elif choice == 0:
        input("Press 'Enter' button to exit...")
