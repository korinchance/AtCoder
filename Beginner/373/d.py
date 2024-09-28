n, m = map(int,input().split())
Z = [[int(z) for z in input().split()] for i in range(m)]
u = 0
v = 1
w = 2

answerlist = [0]*n

for i in range(m):
    if answerlist[Z[i][v]-1]-answerlist[Z[i][u]-1] == Z[i][w]:
        continue
    else:
        if Z[i][v] > Z[i][u]:
            answerlist[Z[i][v]-1] = answerlist[Z[i][u]-1]+Z[i][w]
        else:
            answerlist[Z[i][u]-1] = answerlist[Z[i][v]-1]-Z[i][w]
        
print(*answerlist)
        