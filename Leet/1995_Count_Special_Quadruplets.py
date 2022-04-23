"""
✅ GOOD Array (Skills)
tag: easy, logic
Lookback:
- smart backward iterate
"""
from collections import defaultdict
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        def Kamikakushi():
            """
            https://leetcode.com/problems/count-special-quadruplets/discuss/1446988/JavaC%2B%2BPython3-Real-O(n2)-solution
            https://leetcode.com/problems/count-special-quadruplets/discuss/1456709/Python-99-Clean-Code-Walkthrough-From-O(4)-greater-O(3)-greater-O(2)
            T: O(N^2)
            """
            res = 0
            l = len(nums)
            count = defaultdict(int)
            count[nums[l - 1] - nums[l - 2]] = 1

            for b in range(l - 3, 0, -1):
                for a in range(b - 1, -1, -1):
                    res += count[nums[a] + nums[b]]
                for x in range(l - 1, b, -1):
                    count[nums[x] - nums[b]] += 1
            return res

        return Kamikakushi()

        def fxr():
            """
            Runtime: 1656 ms, faster than 42.11% of Python3 online submissions for Count Special Quadruplets.
            T: O(N&4)
            """
            ans = 0
            L = len(nums)
            for i in range(L):
                for j in range(i + 1, L):
                    for k in range(j + 1, L):
                        for l in range(k + 1, L):
                            if nums[i] + nums[j] + nums[k] == nums[l]:
                                ans += 1
            return ans


sl = Solution()
print(sl.countQuadruplets(nums=[1, 2, 3, 4, 9, 5, 10]))
