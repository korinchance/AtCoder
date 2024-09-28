import math

m = int(input())

n = 20
x = 10
    
place = 0
list = [3**10] * n
count = 0
while True:
    if sum(list) == m:
        answerlist = []
        for s in list:
            answer = int(math.log(s, 3))
            answerlist.append(answer)
        print(n)
        print(*answerlist)
        break
    elif x >= 1:
        x -= 1
        a = 3 ** x
        list[place] = a
    else:
        if place < n-1:
            x = 10
            place += 1
        else:
            x = 10
            place = 0
            n -= 1
            list = [3**10] * n
            
