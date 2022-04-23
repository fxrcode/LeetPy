"""

FB tag (easy)

Daily Challenge (Jan 18)
https://leetcode.com/list?selectedList=5f4y8dwj
Must Do Easy Questions
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, F: List[int], n: int) -> bool:
        def awice():
            """
            Runtime: 233 ms, faster than 26.10% of Python3 online submissions for Can Place Flowers.

            DON'T wordy translate, Do logic translate
            So we don't change n, but use count for plants
            """
            nonlocal F
            count = 0
            F = [0] + F + [0]
            for i in range(1, len(F) - 1):
                if F[i - 1] + F[i] + F[i + 1] == 0:
                    F[i] = 1
                    count += 1
                    if count >= n:
                        return True
            return count >= n

        def fxr2():
            """
            Runtime: 281 ms, faster than 12.95% of Python3 online submissions for Can Place Flowers.

            """
            nonlocal F
            cnt = 0
            F = [1, 0] + F + [0, 1]
            ones = []
            for i, c in enumerate(F):
                if c == 1:
                    ones.append(i)
            for p, c in zip(ones, ones[1:]):
                # analyze cases to find pattern
                cnt += max(0, (c - p - 2)) // 2
            return cnt >= n

        return fxr2()

        def fxr():
            """
            Runtime: 164 ms, faster than 77.50% of Python3 online submissions for Can Place Flowers.

            AC in 1. But no proof
            """
            nonlocal n, F
            F = [0] + F + [0]
            for i in range(1, len(F) - 1):
                if n == 0:
                    return True
                if F[i] == 0 and F[i - 1] + F[i + 1] == 0:
                    F[i] = 1
                    n -= 1
                    if n == 0:
                        return True
            return n == 0

        # return fxr()
        return awice()


sl = Solution()
print(sl.canPlaceFlowers(F=[1, 0, 0, 0, 1], n=1))
print(sl.canPlaceFlowers(F=[1, 0, 0, 0, 1], n=2))
print(sl.canPlaceFlowers([0, 0, 0, 0, 0, 1, 0, 0], 0))
print(sl.canPlaceFlowers([1], 0))
print(sl.canPlaceFlowers([1, 0, 0, 0, 1], 2))
print(sl.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
