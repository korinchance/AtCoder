N, K = list(map(int, input().split()))
a = list(map(int, input().split()))
A = sorted(a)
x = N - K - 1
l = []

for i in range(N-x):
    l.append(A[i+x] - A[i])
    
print(min(l))