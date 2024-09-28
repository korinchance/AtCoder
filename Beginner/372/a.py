s = list(input())
target = '.'
s = [item for item in s if item != target]
print("".join(map(str, s)))