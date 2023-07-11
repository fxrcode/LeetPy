"""
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

"""


from math import log10
from typing import List


class Solution:
    def isArmstrong(self, n: int) -> bool:
        def os_log():
            """
            Runtime: 28 ms, faster than 83.02% of Python3 online submissions for Armstrong Number.

            T: O(n), M: O(1)
            """
            nonlocal n
            k = int(log10(n)) + 1
            result = 0
            v = n
            while n:
                result += pow(n % 10, k)
                n //= 10
            # print(v, result)
            return result == v

        def fxr_brute():
            """
            Runtime: 28 ms, faster than 83.02% of Python3 online submissions for Armstrong Number.

            T: O(n), M:O(n)
            """
            nonlocal n
            v = n
            k = len(str(n))
            sumk = 0
            while n:
                sumk += pow((n % 10), k)
                n //= 10
            return sumk == v
