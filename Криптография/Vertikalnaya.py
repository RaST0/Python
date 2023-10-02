from textwrap import wrap
from random import randint

m1 = input('Введите сообщение для шифрования: ')
m1 = m1.replace(' ', '+')

alph_dor = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.!:;- "'
alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

key_inp = input('Введите ключ: ')
key = []
key2 = []
for i in key_inp:
    key.append( alph.find(i) + 1)


for i in range(len(key)):
    key2.append(key.index(min(key)))
    key[key.index(min(key))] = max(key) + 1
    


length = len(m1)
if len(m1) % len(key2) != 0:
    for i in range(len(key2) - len(m1) % len(key2)):
        m1 += alph_dor[randint(0, len(alph_dor) - 1)]
m1 = wrap( m1, len(key2))
m2 = ''

for i in m1:
    for j in key2:
        m2 += i[j]
        
print('Зашифрованный вид: ', m2.replace('+', ' '))

m2 = wrap(m2, len(key2))

m1 = ''
key = []


for i in range(len(key2)):
    key.append(key2.index(min(key2)))
    key2[key2.index(min(key2))] = max(key2) + 1



for i in m2:
    for j in key:
        m1 += i[j]

print('Расшифрованный вид: ')
m1 = m1.replace('+', ' ')
for i in m1:
    if i == '$':
        break
    print(i, end='')
