s = input()
list = []

for i in range(len(s)):
    for x in range(i+1,len(s)+1):
        list.append(s[i:x])

answerset = set(list)
print(len(answerset))