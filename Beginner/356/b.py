import numpy as np

N, M = list(map(int,input().split()))
A = list(map(int,input().split()))

X = [list(map(int,input().split())) for _ in range(N)]
eatenlist = np.array(X)

nutrition_sumlist = np.sum(eatenlist, axis=0)

koumoku = 0

while koumoku < M:
    if nutrition_sumlist[koumoku] < A[koumoku]:
        print("No")
        break
    else:
        koumoku += 1
if koumoku == M:
    print("Yes")