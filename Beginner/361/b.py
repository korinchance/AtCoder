Rect1 = list(map(int, input().split()))
Rect2 = list(map(int, input().split()))

a = Rect1[0:3]
B = Rect1[3:6]
b = Rect2[0:3]
A = Rect2[3:6]

if b[0] <= a[0] and b[1] <= a[1] and b[2] <= a[2]:
    if A[0] > a[0] and A[1] > a[1] and A[2] > a[2]:
        print('Yes')
    else:
        print('No')
elif b[0] >= a[0] and b[1] >= a[1] and b[2] >= a[2]:
    if B[0] > b[0] and B[1] > b[1] and B[2] > b[2]:
        print('Yes')
    else:
        print('No')
else:
    print('No')