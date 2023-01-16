"""
tag: medium, bisect
date: 01162023
Lookback:
- how to break half (even vs odd). If odd, simply overlap w/ middle, rather break into left, middle, right. So we have unified logic
"""

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader(object):
    # Compares the sum of arr[l..r] with the sum of arr[x..y]
    # return 1 if sum(arr[l..r]) > sum(arr[x..y])
    # return 0 if sum(arr[l..r]) == sum(arr[x..y])
    # return -1 if sum(arr[l..r]) < sum(arr[x..y])
    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        pass

    # Returns the length of the array
    def length(self) -> int:
        pass


class Solution:
    def getIndex(self, reader: "ArrayReader") -> int:
        def htkzmo():
            """
            Runtime: 302 ms, faster than 72.41% of Python3 online submissions for Find the Index of the Large Integer.

            Tricky part: maintain len[l...r] === len[x...y], then compare make sense
            bisect find 1st pos st. compare >= 0: hi = mid (This is important, ow, WA in [1,2,1,1,1,1,1,1,1])
            """
            n = reader.length()
            lo, hi = 0, n - 1

            while lo < hi:
                mid = (lo + hi) // 2
                if (hi - lo + 1) % 2 == 0:
                    cmp = reader.compareSub(lo, mid, mid + 1, hi)
                else:
                    cmp = reader.compareSub(lo, mid, mid, hi)

                if cmp >= 0:
                    hi = mid
                else:
                    lo = mid + 1

            return lo

        def fxr_TLE():
            lo, hi = 0, reader.length() - 1
            while lo < hi:
                mid = (lo + hi) // 2
                even = False
                if (hi - lo + 1) % 2 == 0:
                    even = True
                if even:
                    l, r, x, y = lo, mid, mid + 1, hi
                    if reader.compareSub(l, r, x, y) == 1:
                        hi = mid
                    else:
                        lo = mid + 1
                else:
                    l, r, x, y = lo, mid - 1, mid + 1, hi
                    if reader.compareSub(l, r, x, y) == 0:
                        return mid
                    elif reader.compareSub(l, r, x, y) == 1:
                        hi = mid - 1
                    else:
                        lo = mid + 1
            return lo
