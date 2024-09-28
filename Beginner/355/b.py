N, M = map(int,input().split())
A_list = sorted(list(map(int,input().split())))
B_list = list(map(int,input().split()))
AB_list = A_list + B_list
newAB_list = sorted(AB_list)
x = 0
y = 1
if N < 2:
    print("No")
    exit()
while y < N:
    X = newAB_list.index(A_list[x])
    Y = newAB_list.index(A_list[y])
    if Y - X == 1:
        print("Yes")
        exit()
    x += 1
    y += 1           
print("No")