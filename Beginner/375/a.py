n = int(input())
s = input()
counter = 0

for i in range(1,n-1):
    if s[i] == '.':
        if s[i-1] == s[i+1] == '#':
            counter += 1

print(counter)