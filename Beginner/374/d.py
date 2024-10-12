n, s, t = map(int, input().split())
l = [[int(x) for x in input().split()] for i in range(n)]
counter = 0
import math

for i in range(n):
    a_c = abs(l[i][2]-l[i][0])
    b_d = abs(l[i][3]-l[i][1])
    counter += (math.sqrt(a_c**2+b_d**2))/t
    
counter += (l[0][])