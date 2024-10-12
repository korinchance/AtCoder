h, w = map(int, input().split())
s_h, s_w = map(int, input().split())
c = [[x for x in input()] for i in range(h)]
x = input()

for i in range(len(x)):
    if x[i] == 'L':
        if s_w != 1 and c[s_h-1][s_w-2] == '.':
            s_w -= 1
    elif x[i] == 'R':
        if s_w != w and c[s_h-1][s_w] == '.':
            s_w += 1
    elif x[i] == 'U':
        if s_h != 1 and c[s_h-2][s_w-1] == '.':
            s_h -= 1
    else: #x[i] == 'D'のとき
        if s_h != h and c[s_h][s_w-1] == '.':
            s_h += 1
            
print(s_h,s_w)