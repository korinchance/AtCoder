N, L, R = list(map(int,input().split()))
A = [x for x in range(1,N+1)]

changinglist = A[L-1:R]
changedlist = list(reversed(changinglist))

list1 = A[0:L-1]
list2 = changedlist
list3 = A[R:N]

result = list1 + list2 + list3
print(*result)