n = int(input())
x = list(map(int,input().split()))
p = list(map(int,input().split()))
xp = []
for i in range(n):
    xp_portion = []
    xp_portion.append(x[i])
    xp_portion.append(p[i])
    xp.append(xp_portion)

q = int(input())
l_r = [list(map(int,input().split())) for _ in range(q)]

for i in range(q):
    
#TLE、わかってたけど
#for i in range(q):
#    counter = 0
#    for z in range(n):
#        if l_r[i][0] <= xp[z][0] <= l_r[i][1]:
#            counter += xp[z][1]
#    print(counter)