n = int(input())
h = list(map(int, input().split()))

c = 0

x = h[0]//5
remain = h[0] % 5
if remain == 3 or remain == 4:
    y = 3
elif remain == 2:
    y = 2
elif remain == 1:
    y = 1
else:
    y = 0  
c += (3*x + y)

for i in range(1,len(h)):
    if y == 2:
        h[i] -= 3
        c += 1
    elif y == 1:
        h[i] -= 4
        c += 2 
    
    x = h[i]//5
    remain = h[i] % 5
    if remain == 3 or remain == 4:
        y = 3
    elif remain == 2:
        y = 2
    elif remain == 1:
        y = 1
    else:
        y = 0  
    c += (3*x + y)
        
print(c)