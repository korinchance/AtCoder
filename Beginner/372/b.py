m = int(input())

remain = m
n = 20
a_list = [0]*n
answer_list = []

for i in range(n):
    a = 10
    for x in range(10):
        if remain < 3**a:
            a -= 1
        else:
            break
    a_list[i] = a
    remain -= 3**a
    answer_list.append(a_list[i])
    if remain == 0:
        break
    
print(len(answer_list))
print(*answer_list)