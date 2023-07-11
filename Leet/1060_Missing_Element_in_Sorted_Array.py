"""

tag: medium, bisect
similar: 1539
"""

from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def os_bisect():
            """
            4,7,9,10
            4,5,6,7
            0,2,3,3
            """
            n, n0 = len(nums), nums[0]
            # how many numbers are missing until nums[i]
            missing = lambda i: nums[i] - (n0 + i)
            if k > missing(n - 1):
                return nums[-1] + k - missing(n - 1)
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] - (n0 + m) >= k:
                    r = m
                else:
                    l = m + 1
            return nums[l - 1] + k - missing(l - 1)

        return os_bisect()


sl = Solution()
print(sl.missingElement(nums=[4, 7, 9, 10], k=1))
print(sl.missingElement(nums=[4, 7, 9, 10], k=3))
print(sl.missingElement(nums=[1, 2, 4], k=3))
