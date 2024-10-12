n = int(input())
es =[[x for x in input()]for i in range(n)]

len_list = []
for i in range(n):
    len_list.append(len(es[i]))
max_len = max(len_list)

s = list(reversed(es))
answer_list = []
for i in range(max_len):
    new_str = ''
    for x in range(0,n):
        if i < len(s[x]):
            new_str = new_str + s[x][i]
        else:
            new_str = new_str + '*'
    answer_str = ''.join(new_str)
    answer_list.append(answer_str)

for i in range(len(answer_list)):
    answer_list[i] = answer_list[i].rstrip('*')

print(*answer_list, sep='\n')