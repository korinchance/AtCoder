N = int(input())
LR = [map(int, input().split()) for _ in range(N)]
L, R = [list(i) for i in zip(*LR)]

if sum(L) > 0 or sum(R) < 0:
    print('No')
