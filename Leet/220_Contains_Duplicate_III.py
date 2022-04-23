"""
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1013/
Leetcode Explore Binary Search Tree: Conclusion

tag: medium, SortedContainers
Lookback
- 1st time bisect in SortedContainers
"""


from typing import List

from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def bst():
            """
            Your runtime beats 8.98 % of python3 submissions.

            DBabichev, also modified a bit according to official solution II.
            REF: https://leetcode.com/problems/contains-duplicate-iii/discuss/824603/Python-SortedList-O(n-log-k)-solution-explained.

            XXX: code looks short but actually there's sage in every line!!!
            T: O(Nlogk), M: O(k)
            """
            SList = SortedList()
            for i in range(len(nums)):
                # XXX: before we process nums[i] in this iteration, make sure the left window has size k
                #       because we're searching for elem in range [nums[i]-t, nums[i]+t] in
                #       nums[i]'s left window [nums[i-k]...nums[i-1]], so len(window) = k
                if i > k:
                    # no worry about dup, because SList can have dup. and if dup in window, then dup1-dup2=0 <= t!
                    SList.remove(nums[i - k - 1])
                # XXX: no need to specific handling empty list, obviously, no solution
                # XXX: what are we searching? Ans: in `left window` (notice we don't need
                #       wordly translate to 2k-len window centered at nums[i]) of nums[i]:
                #       [i-k..i), is there element in range [nums[i]-t, nums[i]+t]?
                pos1 = SList.bisect_left(nums[i] - t)
                pos2 = SList.bisect_right(nums[i] + t)
                print(pos1, pos2, nums[i], i, SList)
                # XXX: both bisect_left/right(v) return insertion pos, the difference is
                # e in [:i] < v for left, and <= v for right.
                # if v exists in array, then r-l = # of v in origin array. so l==r means not found.
                if pos1 < pos2:
                    return True
                # XXX: here we processed nums[i], so add nums[i] and remove nums[i-k] so that next iteration,
                #       which process nums[i+1], the left window starts from nums[i-k+1]j
                #       Notice the diff from DBabichev which put remove(nums[i-k-1]) at beginning, because we need
                #       process nums[i+1], so remove outsider nums[i-k-1]
                SList.add(nums[i])
            return False

        def naive_linear_search():
            """
            XXX: come up with brute force,
                a. get partial credit.
                b. find some patterns and get idea how to improve.

            XXX: Official Solution: abs(i-j)<=k === k-sized window
            T: O(n*min(n,k)). M: O(1)
            """

            # O(N)
            for i in range(len(nums)):
                # O(K)
                # XXX: common snippet max(0, i-k), rather if/else
                for j in range(max(0, i - k), i):
                    if abs(nums[i] - nums[j]) <= t:
                        return True
            return False

        # return naive_linear_search()
        return bst()


sl = Solution()
sl.containsNearbyAlmostDuplicate(nums=[7, 1, 9], k=2, t=3)
# sl.containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3)
