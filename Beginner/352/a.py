takahashi = list(map(int,input().split()))
if (takahashi[1] < takahashi[3] < takahashi[2]) or (takahashi[2] < takahashi[3] < takahashi[1]):
    print("Yes")
else:
    print("No")

###review
# n, x, y, z = list(map(int, input().split()))
# if x < z< y or y < z < x:
#     print("Yes")
# else:
#     print("No")