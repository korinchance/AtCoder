#解説あり
n = int(input())
l = [[int(x) for x in input().split()] for i in range(n)]
counter = 0

for i in range(n):
    counter += l[i][0]
    
c = []
for i in range(n):
    c.append(l[i][1]-l[i][0])

counter += max(c)
    
print(counter)