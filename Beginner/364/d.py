N, Q = map(int,input().split())
a = list(map(int,input().split()))
bk = list(map(int,input().split()) for _ in range(Q))
b, k = [list(i) for i in zip(*bk)]
interval_list = []

for i in range(Q):
    for x in range(N):
        interval_element = abs(b[i]-a[x])
        interval_list.append(interval_element)
    sortedinterval_list = sorted(interval_list)
    print(sortedinterval_list[k[i]-1])
    interval_list.clear()