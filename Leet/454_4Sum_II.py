'''
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1134/
Leetcode Explore: Hash Table. Conclusion
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
'''


from typing import List
from collections import Counter


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        Your runtime beats 90.06 % of python3 submissions.

        My re-impl without using generator expression
        """
        list_ab = [a+b for a in nums1 for b in nums2]
        AB = Counter(list_ab)
        ans = 0
        for c in nums3:
            for d in nums4:
                # Your runtime beats 75.79 % of python3 submissions. if I add: if -c-d in AB:
                ans += AB[-c-d]
        return ans

    def fourSumCount_StefanPochmann(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python
        Your runtime beats 93.94 % of python3 submissions.

        XXX: no idea in 1st time. Actually quite simple. Becase a+b+c+d = 0 <=> a+b = -c-d. Then loop c,d to find how many AB[-c-d] exists.
        So O(N^2) time. O(N^2) space
        """
        AB = Counter([(a+b) for a in nums1 for b in nums2])
        return sum(AB[-c-d] for c in nums3 for d in nums4)


sl = Solution()
nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
print(sl.fourSumCount(nums1, nums2, nums3, nums4))
