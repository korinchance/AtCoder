s_ab, s_ac, s_bc = list(map(str,input().split()))

if s_ab == '<' and s_ac == '>' or s_ab =='>' and s_ac == '<':
    print('A')
elif s_ab == '<' and s_bc == '<' or s_ab == '>' and s_bc == '>':
    print('B')
else:
    print('C')