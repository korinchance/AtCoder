N, T, A = map(int,input().split())
interval = abs(T - A)
remainders = N - T - A

if interval > remainders:
    print('Yes')
else:
    print('No')