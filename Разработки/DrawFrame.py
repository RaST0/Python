symbols = "─│┌┐└┘"
symbols.split()
symbols_double = "═║╔╗╚╝"
symbols_double.split()
a = int(input("Ширина:\n"))
b = int(input("Высота:\n"))
c = input("Использовать двойную рамку?\n")
if c == "Да":
    print(symbols_double[2],symbols_double[0]*a,symbols_double[3])
    for i in range(b):
        print(symbols_double[1]," "*a,symbols_double[1])
    print(symbols_double[4],symbols_double[0]*a,symbols_double[5])
if c == "Нет":
    print(symbols[2],symbols[0]*a,symbols[3])
    for i in range(b):
        print(symbols[1]," "*a,symbols[1])
    print(symbols[4],symbols[0]*a,symbols[5])
else:
    print("Введите Да или Нет")
# Убрать пробел в углу