import itertools


data  = open("17.txt").readlines()
sizes = []
ans = []


for line in data:
    sizes.append(int(line))
    
sizes = sorted(sizes)
ways = 0
for i in range(len(sizes)):
    for combo in itertools.combinations(sizes,i):
        if sum(combo) == 150:
            ways+=1
    if ways:
        break
print(ways)
