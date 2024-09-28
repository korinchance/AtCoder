from itertools import permutations

N, K = map(int, input().split())
S = input("")
st = set()
counter = 0

for it in permutations(S):
    st.add("".join(it))
    st_list = list(st)
for i in range(len(st_list)):
    x = 0
    y = x+K+1
    pword = st_list[i]
    while x <= N-K:
        pst = pword[x:y]
        if pst != pst[::-1]:
            x += 1
        else:
            counter += 1
            break
print(len(st_list)-counter)