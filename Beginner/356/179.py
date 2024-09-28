import itertools

N, K = list(map(int,input().split()))
a = list(map(int,input().split()))
A = sorted(a)
newA = [0] + list(itertools.accumulate(A))

if K < 0:
    if K <= max(newA):
       print("Yes")
       print(*A)
    else:
        print("No")       
elif max(newA) >= K:
    print("Yes")
    print(*A)
else:
    print("No")