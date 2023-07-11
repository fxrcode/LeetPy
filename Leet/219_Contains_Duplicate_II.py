"""
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1121/
Leetcode Explore: Hash Table. Practical Application - HashMap
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


"""


from typing import List


class Solution:
    def containsNearbyDuplicate_sol(self, nums: List[int], k: int) -> bool:
        """
        Official solution: T:O(n), M:O(min(n,k))
        """
        nearbyDup = set()  # a k-size window
        for i, n in enumerate(nums):
            if n in nearbyDup:
                return True
            nearbyDup.add(n)
            if len(nearbyDup) > k:
                nearbyDup.remove(nums[i - k])
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Your runtime beats 85.94 % of python3 submissions.
        T: O(n), M: O(n)

        AC in 2nd.
        """
        # what does lr mean after 2 weeks? After read code, I realize it means the left bound of window
        n2lr = {}
        for i, n in enumerate(nums):
            if n in n2lr:
                if i - n2lr[n] <= k:
                    return True
                # XXX: got WA in 1st submit, because I didn't update dict here.
                # if |l-i| > k, then |l - i+k| >> k. so we must update l!
                # logically, we use least-recently seen Policy
                n2lr[n] = i
            else:
                n2lr[n] = i

        return False


sl = Solution()
# nums = [1, 2, 3, 1, ]
# k = 3
# nums = [1, 2, 3, 1, 2, 3]
# k = 2
nums = [1, 0, 1, 1]
k = 1
print(sl.containsNearbyDuplicate_sol(nums, k))
