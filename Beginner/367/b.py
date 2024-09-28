x = input('')

if not x[-1] == '0':
    print(x)
elif not x[-2] == '0':
    print(x[:-1])
elif not x[-3] == '0':
    print(x[:-2])
else:
    print(x[:-4])