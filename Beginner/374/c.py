n = int(input())
k = list(map(int, input().split()))
key = sum(k)/2

import itertools,math
answerlist = []
list = []
x = n

while x >= 1:
    list = list(map(int(itertools.combinations(k, x))))
    l = math.comb(len(k), x)
    for i in range(l):
        if sum(list[i]) >= key:
            answerlist.append(sum(list[i]))
    x -= 1
    
print(min(answerlist))