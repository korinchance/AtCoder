#　chatによる助言あり
n, k = map(int, input().split())
s = input()

blockcounter = 0
idx = 1

while idx < n:
    if s[idx-1] == '1' and s[idx] == '0':
        blockcounter += 1
        if blockcounter == k-1:
            start_idx = idx
        elif blockcounter == k:
            now_end_idx = idx-1
            break
    
    if blockcounter == (k-1) and s[idx-1] == '0' and s[idx] == '1':
        now_start_idx = idx
        
    idx += 1
    
if blockcounter == (k-1) and s[-1] == '1':
    blockcounter += 1
    now_end_idx = n-1  

firstblock = s[0:start_idx]
thirdblock = s[now_end_idx+1:]

number_1 = now_end_idx - now_start_idx + 1
secondblock_1 = '1' * number_1
number_0 = now_end_idx - start_idx + 1 - number_1
secondblock_0 = '0' * number_0

answer = firstblock + secondblock_1 + secondblock_0 + thirdblock

print(answer)
                   
        
            
    
        
    