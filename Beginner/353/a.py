birusuu = int(input())
takasa = list(map(int,input().split()))
n = -1
for i in range(1,len(takasa)):
    if takasa[i] > takasa[0]:
        n = i+1
        break
print(n)

#print(min((i+1 for i in range(1,birusuu) if takasa[i] > takasa[0]),default=-1))