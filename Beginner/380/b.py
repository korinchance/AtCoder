s = input()

counter = 0
answerlist = []

for i in range(len(s)):
    if s[i] == '-':
        counter += 1
    if counter >= 1 and s[i] == '|':
        answerlist.append(counter)
        counter = 0

print(*answerlist)