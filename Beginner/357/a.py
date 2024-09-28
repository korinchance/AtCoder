N, M = list(map(int,input().split()))
Hlist = list(map(int,input().split()))

x = 0
sumHand = 0

while x <= N-1:
    sumHand += Hlist[x]
    x += 1
    if sumHand > M:
        print(x-1)
        exit()
print(N)