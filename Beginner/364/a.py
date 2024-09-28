N = int(input())
S = [input() for i in range(N)]
for i in range(N-1):
    if S[i] == 'sweet':
        if S[i+1] == 'sweet' and i+1 != N-1:
            print('No')
            exit()
print('Yes')