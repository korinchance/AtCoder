N, A = map(int,input().split())
Tlist = list(map(int,input().split()))

Answerlist = []
time = 0

for i in range(N):
    if time >= Tlist[i]:
        time += A
        Answerlist.append(time)
    else: 
        time = Tlist[i]
        time += A
        Answerlist.append(time)

print(*Answerlist, sep='\n')
        
    
    