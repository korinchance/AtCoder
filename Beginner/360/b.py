#chataptあり
s, t = list(map(str, input().split()))

len_s = len(s)

for w in range(len_s):
    for c in range(1, w+1):
        candidate = ""
        for i in range(c-1, len_s, w):
            candidate += s[i]
        if candidate == t:
            print('Yes')
            exit()
            
print('No')