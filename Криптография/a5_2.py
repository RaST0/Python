from random import *
import hashlib

def hash_kvadr(m1):
    h = 0
    for i in m1:
        h += ord(i) % 1000
    return h

def rand_prime():
    while True:
        p = randrange(1103, 1200, 2)
        if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
            return p

def find_e(d, m):
    e = 0
    while not e * d % m == 1:
        e += 1
    return e

def NOD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def vz(D,M):
    if NOD(D,M) == 1:
        return False
    else:
        return True

def get_vz(M):
    D = randrange(1103, 1200, 2)
    while vz(D,M):
        D = randrange(1103, 1200, 2)
    return D

print('Начало генерации ключей ')        
P = rand_prime()
Q = rand_prime()

N = P * Q

M = (P - 1) * (Q - 1)

D = get_vz(M)

E = find_e(D, M)

print('Открытые ключи D,N', D,N)
print('Закрытый ключ E', E)

m1 = input('Введите сообщение для шифрования - ')

h = hash_kvadr(m1)
print(hex(h), ' - исходный хэш')
m2 = h ** D % N
print( hex(m2), ' - подпись' )

if m2 ** E % N == h:
    print('Подпись верна')
