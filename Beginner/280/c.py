s = list(input())
t = list(input())

for i in range(len(s)):
    if s[i] == t[i]:
        continue
    else:
        print(i+1)
        exit()
        
print(len(t))