import numpy as np

H,W = (int(x) for x in input().split())
alist = [list(map(int,input().split(" ")))for _ in range(H)]

Alist = np.array(alist)

sums_along_rows = np.sum(Alist,axis=1)
sums_along_cols = np.sum(Alist,axis=0)

x = 0
y = 0
sumlist = []
for i in range(H*W):
    element_sumlist = sums_along_rows[x] + sums_along_cols[y] - Alist[x,y]
    sumlist.append(element_sumlist)
    y += 1
    if y == W:
        print(*sumlist[-W:])
        y = 0
        x += 1