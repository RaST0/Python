symbols = "─│┌┐└┘"
a = int(input("Введите широту:\n"))
b = int(input("Введите высоту:\n"))
print(symbols[2],"".join(symbols[0] for x in range(5*a)),symbols[3])
for i in range(b):
    print(symbols[1],"".join(" A " +" "+ symbols[1] for x in range(a)))
    print(symbols[1],"".join(symbols[0] for x in range(5*a)),symbols[1])
print(symbols[4],"".join(symbols[0] for x in range(5*a)),symbols[5])

# Убрать в углу симвл