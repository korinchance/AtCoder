n = int(input())
g_m = int(input())
g_v = [list(map(int,input().split())) for i in range(g_m)]
h_g = int(input())
g_ab = [list(map(int,input().split())) for i in range(h_g)]
h_price_list = [list(map(int,input().split())) for i in range(h_g)]
counter = 0

if n <= 2:
    print('0')
    exit()
    
for i in range(h_g):
    if g_ab[i] in g_v:
        continue
    else:
        

        
print(counter)