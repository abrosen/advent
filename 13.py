from itertools import permutations
relations = {}

data = open("13.txt", 'r').read()
data = data.split("\n")
for line in data:
    line = line.strip('.')
    line = line.split()
    val = int(line[3]) if line[2] == 'gain' else -int(line[3])
    a = line[0]
    b = line[-1]
    if a not in relations:
        relations[a] = {}
    relations[a][b] = val
print(relations)


best_smiles = -9999999999999
for seating in permutations(relations.keys()):
    seating = list(seating)
    smiles = 0
    for i in range(0, len(seating) - 1):
        smiles += relations[seating[i]][seating[i + 1]]
        smiles += relations[seating[i + 1]][seating[i]]
    smiles += relations[seating[-1]][seating[0]]
    smiles += relations[seating[0]][seating[-1]]
    if smiles > best_smiles:
        best_smiles = smiles

print(best_smiles)

relations['me'] = {}
for peep in relations.keys():
    relations['me'][peep] = 0
    relations[peep]['me'] = 0


best_smiles = -9999999999999
for seating in permutations(relations.keys()):
    seating = list(seating)
    smiles = 0
    for i in range(0, len(seating) - 1):
        smiles += relations[seating[i]][seating[i + 1]]
        smiles += relations[seating[i + 1]][seating[i]]
    smiles += relations[seating[-1]][seating[0]]
    smiles += relations[seating[0]][seating[-1]]
    if smiles > best_smiles:
        best_smiles = smiles

print(best_smiles)
