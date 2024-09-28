N = int(input())
A = list(map(int,input().split()))
B = []
n = 0
m = 1
for i in range(N-1):
    B.append(A[n] * A[m])
    n += 1
    m += 1
print(*B)