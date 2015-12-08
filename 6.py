SIZE = 1000

grid = [[0] * SIZE for i in range(SIZE)]


def toggle(grid, a, b):
    for i in range(a[0], b[0] + 1):
        for j in range(a[1], b[1] + 1):
            grid[i][j] += 2
            """
            if grid[i][j] == 0:
                grid[i][j] = 1
            else:
                grid[i][j] = 0
            """


def on(grid, a, b):
    for i in range(a[0], b[0] + 1):
        for j in range(a[1], b[1] + 1):
            grid[i][j] += 1


def off(grid, a, b):
    for i in range(a[0], b[0] + 1):
        for j in range(a[1], b[1] + 1):
            grid[i][j] = max(0, grid[i][j] - 1)


instructions = open("6.txt", 'r')
for line in instructions:
    words = line.split()
    if words[0] == "toggle":
        top = list(map(int, words[1].split(",")))
        bottom = list(map(int, words[3].split(",")))
        toggle(grid, top, bottom)
    elif words[1] == 'on':
        top = list(map(int, words[2].split(",")))
        bottom = list(map(int, words[4].split(",")))
        on(grid, top, bottom)
    else:
        top = list(map(int, words[2].split(",")))
        bottom = list(map(int, words[4].split(",")))
        off(grid, top, bottom)

"""
x = [0, 0]
y = [999, 0]


toggle(grid, x, y)
"""
total = 0
for line in grid:
    total += sum(line)

print(total)
