b = int(input("Введите ширину:\n"))
a = int(input("Введите высоту:\n"))
f = input("Закрасить?\n")
char = ('\u2588')
if f=='Нет':
    print(char * a)
    for i in range(b):
        print(char, ' ' * (a - 2), char, sep='')
    print(char * a)
if f=='Да':
    print(char * a)
    for i in range(b):
        print(char * (a) ,)
    print(char * a)