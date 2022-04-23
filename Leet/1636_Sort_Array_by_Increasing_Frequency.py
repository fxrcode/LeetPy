'''
https://leetcode.com/company/google/
Easy
'''
from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        def denisrasulev():
            """
            Runtime: 36 ms, faster than 99.94% of Python3 online submissions for Sort Array by Increasing Frequency.

            Python 3 solution - with process of thinking and improvement
            https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/1065249/Python-3-solution-with-process-of-thinking-and-improvement

            """
            f = Counter(nums)
            return sorted(nums, key=lambda x: (f[x], -x))

        def fxr():
            """
            Runtime: 56 ms, faster than 41.83% of Python3 online submissions for Sort Array by Increasing Frequency.

            T: O(N)
            """
            n2f = [[i, 0] for i in range(-100, 101)]
            for n in nums:
                n2f[n+100][1] += 1
            n2f.sort(key=lambda tu: (tu[1], -tu[0]))

            res = []
            for n, f in n2f:
                if f != 0:
                    res.extend([n]*f)
            return res
        return fxr()


sl = Solution()
print(sl.frequencySort(nums=[1, 1, 2, 2, 2, 3]))
print(sl.frequencySort(nums=[-1, 1, -6, 4, 5, -6, 1, 4, 1]))
