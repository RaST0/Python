#Шифр Цезаря

def crypting(mas_temp, temp_len_mas):
    print()
    print('Введите открытый текст: ')
    open_text = input('Вы -> ')
    open_text = open_text.lower()
    print()
    print('Введите ключ: ')
    key = int(input('Вы -> '))
    crypt_text = ''
    for character in open_text:
        try:
            i = mas_temp.index(character)
            crypt_text += mas_temp[i + key]
        except ValueError:
            print()
            print('Ошибка! -> ' + character)
            print()
        except IndexError:
            i = mas_temp.index(character)
            crypt_text += mas_temp[(i + key) - temp_len_mas]

    return print('Зашифрованный текст: ', crypt_text)
        

def decrypting(mas_temp):
    print()
    print('Введите зашифрованный текст: ')
    crypt_text = input('Вы -> ')
    crypt_text = crypt_text.lower()
    print()
    print('Введите ключ: ')
    key = int(input('Вы -> '))
    open_text = ''
    for character in crypt_text:
        try:
            i = mas_temp.index(character)
            open_text += mas_temp[i - key]
        except ValueError:
            print()
            print('Ошибка! -> ' + character)
            print()

    return print('Расшифрованный текст: ', open_text)

if __name__ == "__main__":
    
    print('Шифр Цезаря')

    mas_alph = ['а','б','в','г','д','е',
                'ж','з','и','й','к','л',
                'м','н','о','п','р','с',
                'т','у','ф','х','ц','ч',
                'ш','щ','ъ','ы','ь','э',
                'ю','я',' ',',','.','!',
                '?']

    len_mas = len(mas_alph)
    #print(len_mas)

    while True:
        print()
        print('Введите "1", чтобы зашифровать текст')
        print('Введите "2", чтобы расшифровать текст')
        print()
        choice = input('Вы -> ')
        if choice == '1':
            print()
            crypting(mas_alph, len_mas)
            print()
            continue
        elif choice == '2':
            print()
            decrypting(mas_alph)
            print()
            continue
