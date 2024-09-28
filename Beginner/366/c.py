q = int(input())
box = []

for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        box.append(query[1])
    if query[0] == 2:
        box.remove(query[1])
    if query[0] == 3:
        print(len(set(box)))