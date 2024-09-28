import numpy as np
 
N, M = map(int,input().split())
S_l = [input() for _ in range(N)]
prenewS = np.char.replace(S_l, 'o','1')
newS = np.char.replace(prenewS, 'x','0')
     
print(newS[0])