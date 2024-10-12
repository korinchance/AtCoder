h, w = map(int,input().split())
l = [[x for x in input()] for i in range(h)]

for i in range(h):
    z = 0
    while z < w-1:
        if l[i][z] == 'T' and l[i][z+1] == 'T':
            l[i][z], l[i][z+1] = 'P', 'C'
            z += 2
        else:
            if l[i][z+1] != 'T':
                z += 2
            else:
                z += 1
                
for answer in l:
    print("".join(answer))