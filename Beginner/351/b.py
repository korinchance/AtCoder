N = int(input())
A = list(input() for i in range(N))
B = list(input() for i in range(N))

for i in range(N):
    if A[i] != B[i]:
        x = i
        break

for i in range(N):
    if A[x][i] != B[x][i]:
        y = i
        break
    
print(x+1, y+1)