"""
Curated common snippet in Leetcode: Array
type: interval, etc
"""
from bisect import bisect_left, bisect_right
from typing import List


def transpose_matrix(Mat: List[List[int]]):
    transpose = zip(*Mat)
    return transpose


def split_odd_even(li):
    """
    932. Beautiful Array
    https://leetcode-cn.com/problems/beautiful-array/solution/piao-liang-shu-zu-by-leetcode/
    """
    n = len(li)
    odd, even = (n + 1) // 2, n // 2
    return odd, even


def prefix_sum(nums):
    """
    * usage: subarray sum: 1124. Longest Well-Performing Interval
        find hole: Google 1-boarded max sqaure
        ...

    """
    P = [0] * (len(nums) + 1)
    for i in range(len(P)):
        P[i + 1] = P[i] + nums[i]

    def q(i, j):
        if not 0 <= i <= j < len(nums):
            raise IndexError("i,j should in range")
        return P[j + 1] - P[i]

    print(P)
    print(q(3, 4))


def take_closest(li, x):
    """[summary]
    1182. Shortest Distance to Target Color
    729. My Calendar I

    Assumes li is sorted. Returns closest value to x.
    If two numbers are equally close, return the smallest number.

    T: O(logN)
    """
    i = bisect_left(li, x)
    if i == 0:
        return li[0]
    if i == len(li):
        return li[-1]
    before = li[i - 1]
    after = li[i]
    if after - x < x - before:
        return after
    else:
        return before


def k_closest(li: list[int], x: float, k: int) -> list[int]:
    """
    973. K closest points to origin
    """
    li.sort(key=lambda v: abs(v - x))
    return li[:k]


def range_count_query():
    """[summary]
    find how many elements in src that are also in qry range
    2080. Range Frequency Queries
    Coinbase: time window, hit counter, etc

    XXX: bisect_left/right === lower/upper_bound in C++ STL
    This is the normal pattern of STL ranges [first, last)
    https://stackoverflow.com/a/41958622/3984911
    """
    src = [2, 4, 5, 5, 5, 9, 9, 13, 20]
    qry = [[1, 5], [2, 5], [5, 5], [19, 100], [0, 1]]

    def up_lower_bound(src: list, qry: tuple):
        lower = bisect_left(src, qry[0])
        upper = bisect_right(src, qry[1])
        print(qry, lower, upper)
        return upper - lower

    for q in qry:
        up_lower_bound(src, q)


def bitmasking_chars():
    """[summary]
    Used in 1286. Iterator for Combination
    """
    s = "abcdef"
    j = 2  # ---> 'c'
    # 001000 (High --to-- Low), so convert j to set bit location by this formuala
    bitmask_j = len(s) - 1 - j


# range_query()
# prefix_sum(nums=[3, -1, 2, -9, 17])
print(k_closest([9, 1, -2, 3, 5], 3.14, 3))
