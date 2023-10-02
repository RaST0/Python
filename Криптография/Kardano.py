from textwrap import wrap
from random import randint

alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.!:;- "'
m1 = input('Введите сообщение для шифрования: ') + '$'
length = len(m1)
if len(m1) % 60 != 0:
    for i in range(60 - len(m1) % 60):
        m1 += alph[randint(0, len(m1) % 60)]
m1 = wrap( m1, 60)
m2 = ''

ans = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
        ]

matrix = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
        ]

key1 = matrix
key2 = []
key3 = key1[::-1]
key4 = []

keys = [key1, key2, key3, key4]

for i in matrix:
    key2.append(i[::-1])

for i in key3:
    key4.append(i[::-1])

iterator = 0
for i in m1:
    for k in range(len(key1)):
        for j in range(len(key1[0])):
            try:
                if key1[k][j] == 1:
                    ans[k][j] = i[iterator]
                    iterator += 1
            except:
                pass

    for k in range(len(key4)):
        for j in range(len(key4[0])):
            try:
                if key4[k][j] == 1:
                    ans[k][j] = i[iterator]
                    iterator += 1
            except:
                pass

    for k in range(len(key3)):
        for j in range(len(key3[0])):
            try:
                if key3[k][j] == 1:
                    ans[k][j] = i[iterator]
                    iterator += 1
            except:
                pass

    for k in range(len(key2)):
        for j in range(len(key2[0])):
            try:
                if key2[k][j] == 1:
                    ans[k][j] = i[iterator]
                    iterator += 1
            except:
                pass

    for k in range(len(key2)):
        for j in range(len(key2[0])):
            m2 += ans[k][j]
    iterator = 0


        
print('Зашифрованный вид: ', m2)
m2 = wrap( m2, 60)
m3 = ''


for i in m2:
    for k in range(len(key1)):
        for j in range(len(key1[0])):
            try:
                if key1[k][j] == 1:
                    m3 += i[k*len(key1[0]) + j]
            except:
                pass

    for k in range(len(key4)):
        for j in range(len(key4[0])):
            try:
                if key4[k][j] == 1:
                    m3 += i[k*len(key1[0]) + j]
            except:
                pass

    for k in range(len(key3)):
        for j in range(len(key3[0])):
            try:
                if key3[k][j] == 1:
                    m3 += i[k*len(key1[0]) + j]
            except:
                pass

    for k in range(len(key2)):
        for j in range(len(key2[0])):
            try:
                if key2[k][j] == 1:
                    m3 += i[k*len(key1[0]) + j]
            except:
                pass

answer = ''
for i in m3:
    if i == '$':
        break
    else:
        answer += i

print('Расшифрованный вид: ', answer)
