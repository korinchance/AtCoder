n = int(input())
a = list(map(int, input().split()))
alist = sorted(a, reverse = True)

if alist[0] >= sum(alist[1:]):
    print(sum(alist[1:]))
else:
    right = []
    left = []
    for i in range(n):
        if sum(right) <= sum(left):
            right.append(alist[i])
        else:
            left.append(alist[i])
    if sum(right) > sum(left):
        print(sum(right)-1)
    elif sum(right) < sum(left):
        print(sum(left)-1)
    else:
        print(sum(right))