N = int(input())
S = [input() for i in range(N)]

answer = 0
for i in range(N):
    if S[i] == 'Takahashi':
        answer += 1

print(answer)
