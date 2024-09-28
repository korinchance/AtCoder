n, m = map(int, input().split())
a = list(map(int, input().split()))

new_a = a + a[:-1]
a_c = 0
interval = 0

while interval < n:
    interval += 1
    for i in range(n):
        if sum(new_a[i:i+interval]) % m == 0:
            a_c += 1
            
print(a_c)