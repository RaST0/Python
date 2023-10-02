from colorama import init
import turtle
init()
def spiral(n):
  out = []
  for i in range(0, n):
    line = []
    out.append(line)
    for x in range(0, n):
      line.append(' ') 
  x_start = 0
  y_start = 0
  x_stop = n
  y_stop = n
  char = ('\033[0;0;42m \033[0m')
  while x_stop >= x_start:
    for x in range(x_start, x_stop):
      out[y_start][x] = char  
    for y in range(y_start + 1, y_stop):
      out[y][x_stop - 1] = char  
    y_start += 2 
    for x in range(x_stop - 1, x_start, -1):
      out[y_stop - 1][x] = char
    y_stop -= 1
    x_start += 1 
    for y in range(y_stop - 1, y_start - 1, -1):
      out[y][x_start] = char
    x_stop -=2
    y_stop -= 1
    x_start += 1
  for y in range(0, n):
    print(''.join(out[y]))
func = input("Какой способ использовать? Черепашку или Аски\n")
if func == "Черепашка":
  a = int(input("Введите ширину:\n"))
  b = int(input("Введите высоту:\n"))
  side = 10*a
  turtle.speed(0)
  for i in range(10*b):
      turtle.forward(side)
      turtle.right(90) 
      side = side - 2
  turtle.exitonclick()
if func == "Аски":
  c = int(input("Введите размер:\n"))
  spiral(c)
else:
  print("Функция не найдена")