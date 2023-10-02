Alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
AlphabetReversed = list(reversed(Alphabet))


def main():
    print("АТБАШ")
    clearText = input('Введите текст: ')
    print("Исходный текст: " + clearText)
    cipherText = cipher(clearText)
    print("Зашифрованный текст: {0}".format(cipherText))
    decipherText = decipher(cipherText)
    print("Расшифрованный текст: {0}".format(decipherText))
    return


def cipher(clearText):
    result = ""
    for c in clearText:
        if c == " ":
            continue
        idx = Alphabet.index(c)
        result += AlphabetReversed[idx]
    return result


def decipher(cipherText):
    result = ""
    for c in cipherText:
        if c == " ":
            continue
        idx = AlphabetReversed.index(c)
        result += Alphabet[idx]
    return result

main()


