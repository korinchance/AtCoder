s = [input() for i in range(12)]
counter = 0

for i in range(1,13):
    if len(s[i-1]) == i:
        counter += 1
        
print(counter)