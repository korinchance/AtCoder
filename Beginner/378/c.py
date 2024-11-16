n = int(input())
a_l = list(map(int,input().split()))
a_dic = {}
b_l = []

for i in range(n):
    a_dic[i+1] = a_l[i]
    
for i in range(n):
    ch_dic = a_dic[:i]

print(a_dic)

print(*b_l)