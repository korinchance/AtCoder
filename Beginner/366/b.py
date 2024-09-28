n = int(input())
s = list(input() for i in range(n))
s.reverse()

def get_maxlength(array):
    maxlength = 0
    for str in array:
        maxlength = max(maxlength, len(str))
    return maxlength
maxlength = get_maxlength(s)

