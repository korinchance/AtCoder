N = int(input())
CP = [map(int,input().split()) for _ in range(N)]
C, P = [list(i) for i in zip(*CP)]
Q = int(input())
LR = [map(int,input().split()) for _ in range(Q)]
L, R = [list(i) for i in zip(*LR)]

for i in range(Q):
    Answerlist1 = []
    Answerlist2 = []
    for x in range(L[i]-1,R[i]):
        if C[x] == 1:
            Answerlist1.append(P[x])
        else:
            Answerlist2.append(P[x])
    print(sum(Answerlist1), sum(Answerlist2))