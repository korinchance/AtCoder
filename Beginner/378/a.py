a = list(map(int, input().split()))
counter = 0
for i in range(1,5):
    if a.count(i) == 4:
        counter += 2
    elif a.count(i) >= 2:
        counter += 1
        
print(counter)