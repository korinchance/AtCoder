n = int(input())
a = list(map(int, input().split()))
distance_list = []
pattern = 0


for i in range(1,len(a)):
    distance_list.append(a[i]-a[i-1])
  
x = 0 
counter = 0   
while x+1 <= (len(distance_list))-1:
    if distance_list[x] == distance_list[x+1]:
        counter += 1
        x += 1
    else:
        if counter >= 1:
            list = []
            for i in range(1,counter+1):
                list.append(i)
            pattern += sum(list)
        x += 1
        counter = 0

if counter >= 1:
    list = []
    for i in range(1,counter+1):
        list.append(i)
    pattern += sum(list)

print(n+(n-1)+pattern)