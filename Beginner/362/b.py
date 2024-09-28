import numpy as np

a_x, a_y = map(int, input().split())
b_x, b_y = map(int, input().split())
c_x, c_y = map(int, input().split())

AB = np.array([b_x-a_x, b_y-a_y])
AC = np.array([c_x-a_x, c_y-a_y])
BC = np.array([c_x-b_x, c_y-b_y])
BA = np.array([a_x-b_x, a_y-b_y])
CA = np.array([a_x-c_x, a_y-c_y])
CB = np.array([b_x-c_x, b_y-c_y])

if np.inner(AB,AC) == 0:
    print('Yes')
elif np.inner(BC,BA) == 0:
    print('Yes')
elif np.inner(CA,CB) == 0:
    print('Yes')
else:
    print('No')