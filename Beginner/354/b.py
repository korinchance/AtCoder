n = int(input())
slist = []
clist = []
for i in range(n):
    s, c = input().split()
    slist.append(s)
    clist.append(int(c))
jishojunn = sorted(slist)
goukeirate = sum(clist)
shousha = jishojunn[goukeirate % n]
print(*[shousha])