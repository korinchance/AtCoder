s = list(input())
t = list(input())
number = len(t)

slist = list(reversed(s))
tlist = list(reversed(t))
answerlist = []

while len(slist) > 0:
    if slist[-1] != tlist[-1]:
        tlist.pop(-1)
    else:
        answerlist.append(number-len(tlist)+1)
        slist.pop(-1)
        tlist.pop(-1)
        
print(*answerlist)