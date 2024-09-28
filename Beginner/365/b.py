N = int(input())
alist = list(map(int, input().split()))

sorted_alist = sorted(alist, reverse=True)
x = sorted_alist[1]

print(alist.index(x)+1)