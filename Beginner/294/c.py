n, m = map(int,input().split())
na = list(map(int,input().split()))
nb = list(map(int,input().split()))

a = sorted(na, reverse=True)
b = sorted(nb, reverse=True)

index_a = []
index_b = []
indexcounter = 1

for i in range(n+m):
    if a and b:
        if a[-1] < b[-1]:
            index_a.append(indexcounter)
            a.pop()
            indexcounter += 1
        else:
            index_b.append(indexcounter)
            b.pop()
            indexcounter += 1
    elif a:
        index_a.append(indexcounter)
        a.pop()
        indexcounter += 1
    else:
        index_b.append(indexcounter)
        b.pop()
        indexcounter += 1
        
print(*index_a)
print(*index_b)
