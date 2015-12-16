import itertools

data = open("9.txt").readlines()

graph = {}

for line in data:
    line = line.split()
    a = line[0]
    b = line[2]
    w = int(line[4])
    if a not in graph:
        graph[a] = {}
    if b not in graph:
        graph[b] = {}
    graph[a][b] = w
    graph[b][a] = w


# Sick, cannot brain today
longest = -1
for path in itertools.permutations(graph.keys()):
    path = list(path)
    length = 0
    for i in range(0,  len(path) - 1):
        length += graph[path[i]][path[i + 1]]
    if length > longest:
        longest = length
print(longest)
