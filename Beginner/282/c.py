n = int(input())
s = list(input())

effect = 'off'
counter = 0

for i in range(n):
    if s[i] == '"':
        counter += 1
        if counter % 2 == 1:
            effect = 'on'
        else:
            effect = 'off'
    elif s[i] == ',':
        if effect == 'on':
            continue
        else:
            s[i] = '.'
    else:
        continue
    
print("".join(s))