'''
Daily Challenge (Feb 8, 2022)
tag: Medium

Lookback:
- variant of Two-Sum.
- need practice more on 2pointer logic: eg. 1996, 1909, etc

[ ] REDO: 2ptr
'''

from collections import Counter
from typing import List
from bisect import bisect_right


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        def os_2ptr():
            """
            Runtime: 104 ms, faster than 54.35% of Python3 online submissions for K-diff Pairs in an Array.

            XXX: so good in logic. 
            core idea is sliding window: expand if y-x < k, contract y-x>k. 
            Careful on y-x=k, and how to prevent count duplicates
            
            T: O(nlogn), M: O(1)            
            """
            nums.sort()
            l, r = 0, 1
            cnt = 0
            while r < len(nums) and l < len(nums):
                if l == r or nums[r] - nums[l] < k:
                    r += 1
                elif nums[r] - nums[l] > k:
                    l += 1
                else:
                    l += 1
                    cnt += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    r = max(r + 1, l + 1)
            return cnt

        return os_2ptr()

        def os_dict():
            """
            Runtime: 76 ms, faster than 85.52% of Python3 online submissions for K-diff Pairs in an Array.

            T: O(N)
            """
            C = Counter(nums)
            res = 0
            for x in C:
                if k > 0 and x + k in C:
                    res += 1
                elif k == 0 and C[x] > 1:
                    res += 1
            return res

        def fxr_sort():
            """
            Runtime: 109 ms, faster than 49.12% of Python3 online submissions for K-diff Pairs in an Array.

            T: O(nlogn)
            """
            cnt = 0
            nums.sort()
            for i, x in enumerate(nums):
                if i != 0 and nums[i - 1] == x:
                    continue
                y = k + x
                j = bisect_right(nums, y)
                if j == 0:  # not found y
                    continue
                if j - 1 == i:  # y and x at same pos
                    continue
                if nums[j - 1] != y:  # not found y
                    continue
                cnt += 1
            return cnt

        def fxr_bf():
            """
            TLE: 52 / 60 test cases passed.
            T: O(N^2), M: O(N)
            """
            pairs = set()
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    a, b = nums[i], nums[j]
                    if a - b == k:
                        pairs.add((a, b))
                    if b - a == k:
                        pairs.add((b, a))
            return len(pairs)


sl = Solution()
# nums = [3, 1, 4, 1, 5]
# nums = [1, 2, 3, 4, 5]
nums = [1, 1, 1, 2, 2]
k = 0
print(sl.findPairs(nums, k))