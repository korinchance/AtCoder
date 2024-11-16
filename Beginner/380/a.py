n = input()

counter_1 = 0
counter_2 = 0
counter_3 = 0

for i in range(len(n)):
    if n[i] == '1':
        counter_1 += 1
    elif n[i] == '2':
        counter_2 += 1
    elif n[i] == '3':
        counter_3 += 1

if counter_1 == 1 and counter_2 == 2 and counter_3 == 3:
    print('Yes')
else:
    print('No')