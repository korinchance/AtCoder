#2024/06/29
N = int(input())
S = input("")
Slist = list(S)

preAnswer = 1
x = 0

while x < N-2:
    if Slist[x] != Slist[x+1] and Slist[x] == Slist[x+2]:
        Answerportion = 2
        x += 2
        while True:
            if x < N-2 and Slist[x] != Slist[x+1] and Slist[x] == Slist[x+2]:
                    Answerportion += 1
                    x += 2
            else:
                preAnswer *= Answerportion
                x += 1
                Answerportion = 0
                break
    else:
        x += 1
Answer = preAnswer % (10**9+7)
print(Answer)