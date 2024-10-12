n = int(input())
xys = [[int(z) for z in input().split()] for i in range(n)]
counter = 0

import math
def square_root(x, y):
     return math.sqrt(x**2+y**2)
 
l = [[0,0]] + xys + [[0,0]]

for i in range(1,len(l)):
    x = l[i][0]-l[i-1][0]
    y = l[i][1]-l[i-1][1]
    counter += square_root(x, y)
    
print(counter)