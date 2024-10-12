#ひろむあり
n = int(input())
a = list(map(int,input().split()))
w = list(map(int,input().split()))
a_w = {}

answer = sum(w)

for i in range(n):
    if not a[i] in a_w:
        a_w[a[i]] = [w[i]]
    else:
        a_w[a[i]].append(w[i])
    
for values in a_w.values():
    answer -= max(values)
    
print(answer)