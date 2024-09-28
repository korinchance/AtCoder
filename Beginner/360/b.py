S, T = input().split()
Slist = list(S)
Tlist = list(T)
x = len(T)-1
sumlist = []

for i in range(len(T)):
    if Tlist[i] not in Slist:
        print('No')
        exit()
if len(T) == 1:
    if T == Slist[len(S)-1]:
        print('No')
    else:
        print('Yes')
else:
    for i in range(len(T)):
        
    
        
