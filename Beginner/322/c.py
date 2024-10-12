#解説書き換え
# 入力を受け取る
n, m = map(int, input().split())
a = list(map(int, input().split()))

# 0-indexedに変換
a = [x - 1 for x in a]

# b配列の初期化
b = [0] * (n + 1)

# b配列に花火の発生回数をカウント
for i in range(m):
    b[a[i] + 1] += 1

# 累積和を計算
for i in range(1, n + 1):
    b[i] += b[i - 1]
print(b)

# 各日についての結果を計算
for i in range(n):
    ok, ng = n, i - 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if b[mid + 1] - b[i] >= 1:
            ok = mid
        else:
            ng = mid
    print(ok - i)


        

    

#for i in range(1,n+1):
#    if not i in a_s:
#        print(min(a_s)-i)
#    else:
#        print(0)
#        a_s.remove(i)

#import bisect
#for i in range(1,n+1):
#    if i in a_s:
#        print(0)
#    else:
#        position = bisect.bisect(a_s, i)
#        print(a_s[position]-i)