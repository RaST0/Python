
import random

from numpy import mat

import random
import numpy as np
char = "■□☺♥" # ■ - Стена ( Нельзя сломать ), □ - Стена ( Можно сломать ), ☺ - Игрок, ♥ - Аптечка
print("---Параметры карты---")
n = int(input("Введите ширину карты:\n"))
m = int(input("Введите высоту карты:\n"))
Matrix = [[random.choice(char) for j in range(m)] for i in range(n)]
print("---Ваша карта---")
print(np.array(Matrix),"\n")
# Без квадратных свобочек