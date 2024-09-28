N,K =(int (x) for x in input().split())
A = list(map(int,input().split()))
olda =[i for i in A if i%K == 0]
newa = [y//K for y in olda]
print(*newa)