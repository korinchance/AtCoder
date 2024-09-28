S = input()
l_number = sum(map(str.isupper,S))
s_number = sum(map(str.islower,S))

if l_number > s_number:
    Answer = S.upper()
else:
    Answer = S.lower()
print(Answer) 