n, k = map(int, input().split())
r = list(map(int, input().split()))

a_l = [1] * n

while True:
    if sum(a_l) % k == 0:
        print(*a_l)
    
    if a_l == r:
        break
    
    x = len(a_l) - 1
    while x >= 0:
        if a_l[x] < r[x]:
            a_l[x] += 1
            break
        else:
            a_l[x] = 1
            x -= 1