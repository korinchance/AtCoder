s = input()
a_to_z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
counter = 0

for i in range(1,26):
    index1 = s.index(a_to_z[i-1])
    index2 = s.index(a_to_z[i])
    if index1 < index2:
        add = (index2-index1)
    else:
        add = (index1-index2)
    counter += add

print(counter)