#カンニング
n = int(input())
a = list(map(int,input().split()))
sorted_a = sorted(a)
counter = 0

for i in range(n-1):
    if sorted_a[i] == sorted_a[i+1]:
        sorted_a[i] = sorted_a[i+1] = 0
        counter += 1
        
print(counter)