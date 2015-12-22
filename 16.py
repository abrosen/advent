sample_text = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
sample_text= sample_text.split("\n")
sample =  {}
for line in sample_text:
    line =  line.split()
    sample[line[0]] = int(line[1])
  
  
print(sample)


def part2(key, val):
    if key == "cats:" or key == "trees:":
        return sample[key] < val
    if key == "pomeranians:" or key == "goldfish":
        return sample[key] > val
    return sample[key] == val

data = open("16.txt",'r').readlines()
for line in data:
    line = line.split()
    
    
    if sample[line[2]] == int(line[3].strip(",")) and sample[line[4]] == int(line[5].strip(",")) and sample[line[6]] == int(line[7].strip(",")) :
        print(line)
        
        
for line in data:
    line = line.split()
    
    
    if part2(line[2], int(line[3].strip(","))) and part2(line[4], int(line[5].strip(","))) and part2(line[6], int(line[7].strip(","))):
        print(line)
