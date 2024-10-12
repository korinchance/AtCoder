n = int(input())
answerlist = []
for i in range(n):
    if (i+1)%3 == 0:
        answerlist.append('x')
    else:
        answerlist.append('o')
str(answerlist)
print(''.join(map(str,answerlist)))