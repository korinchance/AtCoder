s = list(input())
s_set = set(s)
s_set_list = list(s_set)
c_list = []

for i in range(len(s_set)):
    c = s.count(s_set_list[i])
    c_list.append(c)
    
for i in range(1,len(s)+1):
    if c_list.count(i) != 0 and c_list.count(i) != 2:
        print('No')
        exit()

print('Yes')