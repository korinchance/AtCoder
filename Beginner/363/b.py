N, T, P = map(int, input().split())
Llist = list(map(int, input().split()))

if sum([i >= T for i in Llist]) >= P:
    print('0')
else:
    newLlist = sorted(Llist, reverse=True)
    print(T-newLlist[P-1])