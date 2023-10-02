# Zakharov N.A.
# 16.02.2018
import random
 
WORDS = ("питон", "программирование", "винда", "линукс")
 
# Выбор случайного слова из кортежа.
word = random.choice(WORDS)
# Копирование в переменную выбранного случайным образом слова.
correct = word
 
# Приветствие игрока.
print("Добро пожаловать в игру Угадай слово! Компьютер загадывает слово и Вам нужно его угадать. У Вас есть 5 попыток узнать, есть ли какая-то буква в слове,после чего нужно попытаться угадать слово. Удачи!"
)
 
print("Загаданное слово содержит {} букв.".format(len(correct)))
 

tries = 1
 

while True:
    if tries <= 5:
        letter = input("\nВведите букву: ")
        if letter.isalpha() and len(letter) == 1:
            if letter in correct:
                print("Да, такая буква есть в слове.")
                tries += 1
            else:
                print("Нет, такой буквы нет в слове.")
                tries += 1
        else:
            print("Возможно, Вы ввели не букву.")
            # continue
    else:
        tries = 1
        break
 

while True:
    if tries <= 5:
        guess = input("\nТеперь постарайтесь угадать слово: ")
        if not guess.isalpha():
            print("Возможно, Вы не ввели слово.")
        elif guess != correct:
            print("Попробуйте еще раз. Количество оставшихся попыток: {}".format(5 - tries))
            tries += 1
        elif guess == correct:
            print("Вы угадали слово!")
            break
    else:
        print("Вы проиграли.")
        break
 
input("\n\nНажмите Enter для выхода.")


