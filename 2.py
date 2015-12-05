
data  =  open("input2.txt")
sArea =  0
rlength = 0
for line in data:
    dims = line.strip().split('x')
    l,w,h = tuple(map(int,dims))
    # print(l,w,h)
    sArea +=  2*l*w +2*w*h + 2*l*h + min(l*w,w*h,h*l)
    rlength += min(2*l +2*w, 2*w + 2*h, 2*h + 2*l) +l*w*h
print(sArea)
print(rlength)
