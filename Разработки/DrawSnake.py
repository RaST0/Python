from colorama import init
init()
colored = input("Закрасить змейку?\n")
b = int(input("Введите высота:\n"))
a = int(input("Введите ширина:\n"))
char = ('*')
k = 0
char_colored = ('\033[0;0;42m \033[0m')
if colored == 'Да':
    print(char_colored * a)
    for i in range(b):
        if i % 2 == 0:
            if k % 2 ==0:
                print(' ' * (a - 2), char_colored)
                k = k + 1
            else:
                print(char_colored)
                k = k + 1
        else:
            print(char_colored * a)
else:
    print(char * a)
    for i in range(b):
        if i % 2 == 0:
            if k % 2 ==0:
                print(' ' * (a - 2), char)
                k = k + 1
            else:
                print(char)
                k = k + 1
        else:
            print(char * a)
