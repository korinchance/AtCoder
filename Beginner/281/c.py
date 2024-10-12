n, t = map(int,input().split())
a = list(map(int,input().split()))

p_t = t
c = p_t//sum(a)
p_t -= sum(a)*c

song = 1   
while True:
    if p_t > a[song-1]:
        p_t -= a[song-1]
        song += 1
    else:
        print(song, p_t)
        break