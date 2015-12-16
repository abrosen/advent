data = open("8.txt", 'r')
a = 0
b = 0
for line in data:
    line = line.strip()
    x = len(line) + line.count("\"") + line.count("\\") + 2
    y = len(line)
    print(x, y)
    a += x
    b += y

print(a, b, a - b)
