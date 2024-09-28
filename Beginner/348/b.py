n = int(input())
list = [[int(x) for x in input().split()] for i in range(n)]

import math
   
for i in range(n):
    farthlist = []
    for s in range(n):
        farth = math.sqrt((list[s][0]-list[i][0])**2 + (list[s][1]-list[i][1])**2)
        farthlist.append(farth)
    answerelement = max(farthlist)
    print(farthlist.index(answerelement)+1)