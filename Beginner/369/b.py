n = int(input())
l = list()
r = list()
l_counter = 0
r_counter = 0

for i in range(n):
    a, hand = input().split()
    if hand == 'L':
        l.append(int(a))
    else:
        r.append(int(a))

if len(l) >= 2:
    for i in range(1, len(l)):
        l_counter += abs(l[i] - l[i-1])
    
if len(r) >= 2:
    for i in range(1, len(r)):
        r_counter += abs(r[i] - r[i-1])   

print(l_counter+r_counter)   