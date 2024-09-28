n, m = map(int,input().split())

child_list = [input().split() for i in range(m)]
m1_house_list = []

for i in range(m):
    if child_list[i][1] == 'M':
        if not child_list[i][0] in m1_house_list:
            print('Yes')
            m1_house_list.append(child_list[i][0])
        else:
            print('No')
    else:
        print('No')