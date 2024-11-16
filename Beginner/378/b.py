n = int(input())
g_l = [[int(x) for x in input().split()] for i in range(n)]
q = int(input())

for i in range(q):
    t, d = map(int,input().split())
    garbage = g_l[t-1]
    if d <= garbage[1]:
        print(garbage[1])
    else:
        list = range(garbage[1],d,garbage[0])
        print(list[-1]+garbage[0])