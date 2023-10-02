def pause():
    programPause = input("Нажмите <ENTER> для продолжения...")

alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alph2 = alph.upper()

m1 = input('Введите открытый текст: ')
m2 = ''
k = 0
for i in m1: #блок шифрования
    if i.isupper():
        m2 += alph2[(alph2.find(i) + k) % len(alph2)]
    elif i.islower():
        m2 += alph[(alph.find(i) + k) % len(alph)]
    else:
        m2 += i
    k += 1

print('Зашифрованный текст:', m2)

m1 = ''
k = 0

for i in m2:
    if i.isupper():
        m1 += alph2[(alph2.find(i) - k) % len(alph2)]
    elif i.islower():
        m1 += alph[(alph.find(i) - k) % len(alph)]
    else:
        m1 += i
    k += 1
    
print('Расшифрованный текст:', m1)

pause()