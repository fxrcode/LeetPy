"""
✅ GOOD Hash (Counting)
Tag: Medium, Hash
Lookback:
- from 1679
- Counting problem, we can pre-populate Counter. Or better, we can runtime update Counter.
"""

from collections import Counter
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        def ye15_1pass():
            """
            Runtime: 4326 ms, faster than 17.85% of Python3 online submissions for Count Good Meals.
            https://leetcode-cn.com/problems/count-good-meals/solution/gong-shui-san-xie-xiang-jie-san-chong-gu-nn4f/
            ! Crux: runtime update counter, is common trick in counting problem
            """
            freq = Counter()
            res = 0
            for x in deliciousness:
                for k in range(22):
                    res += freq[2**k - x]
                freq[x] += 1
            return res % (10**9 + 7)

        def fxr():
            """
            Runtime: 1588 ms, faster than 52.27% of Python3 online submissions for Count Good Meals.

            T: O(22n)
            """
            freq = Counter(deliciousness)
            res = 0
            for n in freq:
                for k in range(22):
                    o = 2**k - n
                    if o in freq:
                        if o != n:
                            res += freq[n] * freq[o]
                        else:
                            res += freq[n] * (freq[n] - 1)
                        # print(n, o, freq[n], freq[o], res)

            return (res // 2) % (10**9 + 7)

        return fxr()


sl = Solution()
print(sl.countPairs(deliciousness=[1, 3, 5, 7, 9]))
print(sl.countPairs(deliciousness=[1, 1, 1, 3, 3, 3, 7]))
