A, B = map(int,input().split())
hannin_list = [1, 2, 3]
if A == B:
    print(-1)
elif A+B == 5:
    print(hannin_list[0])
elif A+B == 4:
    print(hannin_list[1])
else:
    print(hannin_list[2])