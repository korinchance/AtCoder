n, k = list(map(int,input().split()))
a = list(map(int,input().split()))
count = 0
x = 0
for i in range(n):
    if x + a[i] <= k:
        x += a[i]
    else:
        count += 1 
        x = a[i]
print(count+1)

