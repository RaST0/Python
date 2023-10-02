from random import *

width = int(input("Введите длину лабиринта:\n"))
height = int(input("Введите высоту лабиринта:\n"))
def draw_maze(w,h):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    border_vertical = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    border_horizontal = [["+--"] * w + ['+'] for _ in range(h + 1)]
    def walk(x, y):
        vis[y][x] = 1
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: border_horizontal[max(y, yy)][x] = "+  "
            if yy == y: border_vertical[y][max(x, xx)] = "   "
            walk(xx, yy)
    walk(randrange(w), randrange(h))
    s = ""
    for (a, b) in zip(border_horizontal, border_vertical):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s
print(draw_maze(width,height))