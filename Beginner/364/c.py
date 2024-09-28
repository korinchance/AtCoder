N, X, Y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

Alist = sorted(A, reverse = True)
Blist = sorted(B, reverse = True)
x = 0
y = 0
x_c = 0
y_c = 0

if sum(Alist) <= X:
    x_c = N
else:
    while x <= X:
        x += Alist[x_c]
        x_c += 1
        
if sum(Blist) <= Y:
    y_c = N
else:
    while y <= Y:
        y += Blist[y_c]
        y_c += 1     
    
if x_c <= y_c:
    print(x_c)
else:
    print(y_c)