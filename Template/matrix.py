'''
48. Rotate Image (clockwise 90 deg), Two solutions
XXX: must able to blindly rotate/transpose/reverse
    * Four crux:
        0. use n-1 in indexing!
        1. (r,c) of related points in rotate, transpose, reverse
        2. careful to select points! don't shift & re-shift!
        3. for k-d list, needs deepcopy, since copy() don't create new sublist!
XXX: !use deeeep copy!
'''
from copy import deepcopy

# M = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# M = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 'A', 'B', 'C'], ['D', 'E', 'F', 'G']]
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# M = [[1, 2], [3, 4]]


def pri_m(m):
    for r in m:
        print(r)
    print("--------------------------")


def transpose(m):
    m = deepcopy(m)
    for r in range(len(m)):
        # for c in range(len(m[0])):
        for c in range(r, len(m[0])):
            m[r][c], m[c][r] = m[c][r], m[r][c]
    pri_m(m)


def transpose_other(m):
    m = deepcopy(m)
    n = len(m)
    for r in range(len(m)):
        # for c in range(len(m[0])):
        for c in range(0, len(m[0])-r):
            m[r][c], m[n-c-1][n-r-1] = m[n-c-1][n-r-1], m[r][c]
    pri_m(m)


def reverse(m):
    m = deepcopy(m)
    n = len(m)
    for i in range(len(m)):
        for j in range(n//2):
            m[i][j], m[i][n-j-1] = m[i][n-j-1], m[i][j]
    pri_m(m)


def reverse_up_down(m):
    m = deepcopy(m)
    n = len(m)
    for j in range(len(m)):
        for i in range(n//2):
            m[i][j], m[n-1-i][j] = m[n-1-i][j], m[i][j]
    pri_m(m)


pri_m(M)
transpose(M)
reverse(M)
transpose_other(M)
reverse_up_down(M)
