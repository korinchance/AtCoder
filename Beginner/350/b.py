n, q = map(int, input().split())
tlist = list(map(int, input().split()))
counter = 0

for i in range(1, n+1):
    if tlist.count(i) % 2 == 1:
        counter += 1
        
print(n-counter)