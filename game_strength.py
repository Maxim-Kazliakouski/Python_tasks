# необходимо завязать силы с очками через ключ-значение, а также добавить прибавление или убавление силы! Переделать
# набор сил через словарь
skills = ["Strength", "Health", "Wisdom", "Dexterity", "Remaining points"]
nabor_sil = {"Strength": 0,
             "Health": 0,
             "Wisdom": 0,
             "Dexterity": 0}
limit = 30
points = 30
#   kol_points = int(len(points))
ostatok_point = 30
ochki_ost = 30
choice = None
while choice != "3":
    print("CHOOSE YOUR DESTINY!")
    print("Выберети пункт, чтобы вы хотели сделать:")
    print("1 - показать список сил" "\n" "2 - оставшиеся очки" "\n" "3 - выход из приложения", end="\n")
    print("4 - показать распределённые силы")
    choice = input("Введите пункт меню: ")
    if choice == "1":
        print("Вот список сил, которые имеются на данный момент:")
        print("1 - Strength" "\n" "2 - Health" "\n" "3 - Wisdom" "\n" "4 - Dexterity" "\n")
        choice = int(input("Выберите номер силы, параметры которой Вы хотели бы изменить: "))
        if skills[choice-1] in skills:
            print("Вы выбрали", skills[choice-1])
            print("Необходимо прибавить или убавить данный навык?")
        operacia = input("Введите '+' для того, чтобы прибавить навык и '-' для того, чтобы убавить: ")
        if operacia == "+":
            change_point = int(input("Введите количество поинтов, на которое наеобходимо увеличить ресурс: "))
            # добавить присвоение значения в параметр ключ-значение данного параметра
            ostatok_point = points - change_point
            points = ostatok_point
            if 0 <= points <= limit:
                print("У вас осталось", ostatok_point, "pts")
                # перезаписываем в словаре знечение ключа на новое
                nabor_sil[skills[choice-1]] += change_point
                print("Сейчас навык", skills[choice-1], "имеет", nabor_sil.get(skills[choice-1]), "pts")
                input("Пожалуйста, нажмите Enter для перехода в главное меню...")
            else:
                print("К сожалению введённое вами количество поинтов =", change_point, "превышает допустимый ", end="")
                print("лимит в", limit, "pts!")
                input("Пожалуйста, нажмите Enter для перехода в главное меню...")
        elif operacia == "-":
            change_point = int(input("Введите количество поинтов, на которое наеобходимо уменьшить ресурс: "))
            ostatok_point = points + change_point
            points = ostatok_point
            if 0 <= points <= limit:
                print("У вас осталось", ostatok_point, "pts")
                nabor_sil[skills[choice-1]] -= change_point
                print("Сейчас навык", skills[choice-1], "имеет", nabor_sil.get(skills[choice-1]), "pts")
                input("Пожалуйста, нажмите Enter для перехода в главное меню...")
            else:
                print("К сожалению введённое вами количество поинтов =", change_point, "превышает допустимый ", end="")
                print("лимит в", limit, "pts!")
                input("Пожалуйста, нажмите Enter для перехода в главное меню...")
    if choice == "2":
        print("У вас осталось", points, "pts")
        input("Пожалуйста, нажмите Enter для перехода в главное меню...")
    if choice == "3":
        input("Нжамите Enter для выхода из программы...")
    if choice == "4":
        for key in nabor_sil:
            print(key, "--->", nabor_sil[key], "pts")
        input("Пожалуйста, нажмите Enter для перехода в главное меню...")