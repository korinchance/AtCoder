Takahashi = int(input())
Plant = 0
n = 0
for i in range(Takahashi):
    Plant += 2 ** n
    if Plant <= Takahashi: 
        n += 1
    else:
        break
print(n+1)