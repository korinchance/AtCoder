s_s = list(input())
counter = 0
counter += len(s_s)
for i in range(len(s_s)-1):
    if s_s[i] == s_s[i+1] == '0':
        s_s[i] = s_s[i+1] = 'x'
        counter -= 1

print(counter)