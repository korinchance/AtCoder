s = input()

if s[-3:] == '000' or s[-3:] == '316' or int(s[-3:]) >= 350:
    print('No')
else:
    print('Yes')