n, k = map(int, input().split())
a = list(map(int, input().split()))

downlist = a[0:n-k]
uplist = a[n-k:n]
answerlist = uplist + downlist
print(*answerlist)