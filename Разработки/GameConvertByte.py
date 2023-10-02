
import random
import time
level = input("Выберите уровень сложности:")
question_counter = int(input("Ведите кол-во вопросов:"))
gamemode = int(input("Введите систему счисления: 1. Dec 2. Hex\n"))
t_counter = 0
f_counter = 0

if gamemode == 1: # DEC
    start_time = time.time()
    if level == "child":
        for i in range(question_counter):
            child = random.randint(0,7)
            print(bin(child),"= ? dec ( Ответ:",child,")")
            answer = input("Ваш ответ:\n")
            if answer == str(child):
                t_counter += 1
            else:
                f_counter += 1
    if level == "easy":
        for i in range(question_counter):
            easy = random.randint(0,15)
            print(bin(easy),"= ? dec ( Ответ:",easy,")")
            answer = input("Ваш ответ:\n")
            if answer == str(easy):
                t_counter += 1
            else:
                f_counter += 1
    if level == "medium":
        for i in range(question_counter):
            medium = random.randint(0,63)
            print(bin(medium),"= ? dec ( Ответ:",medium,")")
            answer = input("Ваш ответ:\n")
            if answer == str(medium):
                t_counter += 1
            else:
                f_counter += 1
    if level == "hard":
        for i in range(question_counter):
            hard = random.randint(0,255)
            print(bin(hard),"= ? dec ( Ответ:",hard,")")
            answer = input("Ваш ответ:\n")
            if answer == str(hard):
                t_counter += 1
            else:
                f_counter += 1
    else:
        SystemExit

if gamemode == 2: # HEX
    start_time = time.time()
    if level == "child":
        for i in range(question_counter):
            child = random.randint(0,7)
            print(bin(child),"= ? hex ( Ответ:",hex(child),")")
            answer = input("Ваш ответ:\n")
            if answer == hex(child):
                t_counter += 1
            else:
                f_counter += 1
    if level == "easy":
        for i in range(question_counter):
            easy = random.randint(0,15)
            print(bin(easy),"= ? hex ( Ответ:",hex(easy),")")
            answer = input("Ваш ответ:\n")
            if answer == hex(easy):
                t_counter += 1
            else:
                f_counter += 1
    if level == "medium":
        for i in range(question_counter):
            medium = random.randint(0,63)
            print(bin(medium),"= ? hex ( Ответ:",hex(medium),")")
            answer = input("Ваш ответ:\n")
            if answer == hex(medium):
                t_counter += 1
            else:
                f_counter += 1
    if level == "hard":
        for i in range(question_counter):
            hard = random.randint(0,255)
            print(bin(hard),"= ? hex ( Ответ:",hex(hard),")")
            answer = input("Ваш ответ:\n")
            if answer == hex(hard):
                t_counter += 1
            else:
                f_counter += 1
    else:
        SystemExit
print("--------Статистика--------")
print("Верно:", t_counter)
print("Не верно:", f_counter)
print("Время решения: %s секунд!" % (time.time() - start_time))

