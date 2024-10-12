s = input()
t = input()

if s == t:
    print('0')
    exit()
    
if len(s) > len(t):
    l = len(t)
else:
    l = len(s)

for i in range(l):
    if s[i] != t[i]:
        print(i+1)
        exit()
        
print(l+1)