# Zakharov N.A.
# 16.02.2018

print("""Вам будут представлены изначальные характеристики героя: Сила, Здоровье, Мудрость и Ловкость.
Вам нужно будет, как в ролевой игре, распределить 30 очков между навыками""")
 
# Объявляем переменные.
strength = 0
health = 0
wisdom = 0
agility = 0
choice = None
global_choice = None
 
while global_choice != 0:
 
    # Вывод актуальной таблицы после действия.
    ost_points = (30 - strength - health - wisdom - agility)
    print("Таблица характеристик на данный момент: \n"
        "\t\t\t1. Сила:", strength, "\n"
        "\t\t\t2. Здоровье:", health, "\n"
        "\t\t\t3. Интелект:", wisdom, "\n"
        "\t\t\t4. Ловкость:", agility, "\n\n"
        "\t\t\tСвободное количество очков:", ost_points, "\n")
 
    # Первый выбор
    print("Что вы хотите сделать сейчас?\n"
        "\t\t\t1. Добавить очки в одну из характеристик.\n"
        "\t\t\t2. Убрать очки из характеристики.\n"
        "\t\t\t3. Закончить распределиние очков.\n")
    global_choice = int(input())
    if global_choice == 1:
        print("В какую из характеристик вы хотите добавить очки?\n"
            "\t\t\t1. Сила.\n"
            "\t\t\t2. Здоровье.\n"
            "\t\t\t3. Интелект.\n"
            "\t\t\t4. Ловкость.\n")
        choice = int(input())
        if choice == 1:
            print("Сколько очков вы хотите добавить?\n")
            scores = int(input())
            if scores >= 0 and scores <= ost_points:
                strength += scores
            else:
                print("Недопустимое количество очков.\n")
        elif choice == 2:
            print("Сколько очков вы хотите добавить?\n")
            scores = int(input())
            if scores >= 0 and scores <= ost_points:
                health += scores
            else:
                print("Недопустимое количество очков.\n")
        elif choice == 3:
            print("Сколько очков вы хотите добавить?\n")
            scores = int(input())
            if scores >= 0 and scores <= ost_points:
                wisdom += scores
            else:
                print("Недопустимое количество очков.\n")
        elif choice == 4:
            print("Сколько очков вы хотите добавить?\n")
            scores = int(input())
            if scores >= 0 and scores <= ost_points:
                agility += scores
            else:
                print("Недопустимое количество очков.\n")
 
    # Второй выбор
    elif global_choice == 2:
        print("Из какой характеристики вы хотите убрать очки?\n"
            "\t\t\t1. Сила.\n"
            "\t\t\t2. Здоровье.\n"
            "\t\t\t3. Интелект.\n"
            "\t\t\t4. Ловкость.\n")
        choice = int(input())
        if choice == 1:
            print("Сколько очков вы хотите убрать?\n")
            scores = int(input())
            if scores >= 0 and (strength - scores) >= 0:
                strength -= scores
            else:
                print("Недопустимое количество очков.\n")
        elif choice == 2:
            print("Сколько очков вы хотите убрать?\n")
            scores = int(input())
            if scores >= 0 and (health - scores) >= 0:
                health -= scores
            else:
                print("Недопустимое количество очков.\n")
        elif choice == 3:
            print("Сколько очков вы хотите убрать?\n")
            scores = int(input())
            if scores >= 0 and (wisdom - scores) >= 0:
                wisdom -= scores
            else:
                print("Недопустимое количество очков.\n")
        elif choice == 4:
            print("Сколько очков вы хотите убрать?\n")
            scores = int(input())
            if scores >= 0 and (agility - scores) >= 0:
                agility -= scores
            else:
                print("Недопустимое количество очков.\n")
    # Третий выбор. Проверяем, все ли очки использованы.
    elif global_choice == 3:
        if ost_points == 0:
            print("Ваш герой готов! Таблица его характеристик выглядит так: \n"
    "\t\t\t1. Сила:", strength, "\n"
    "\t\t\t2. Здоровье:", health, "\n"
    "\t\t\t3. Интелект:", wisdom, "\n"
    "\t\t\t4. Ловкость:", agility, "\n")
            break
        else:
            print("Используйте все очки, данные вам!\n")
input("\n\nНажмите Enter, чтобы выйти.")
