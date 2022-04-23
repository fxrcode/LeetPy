"""
✅ GOOD Bisect (division type)
tag: Hard, bisect
Lookback
- Weekly Premium (Mar W4, 2022)
https://docs.google.com/presentation/d/1fnjMW_vcm-5R6KYwBujRz_CrGkOv9u8vS0NLNqG-0Kk/edit#slide=id.g879e03f1fc_0_0
Generic Binary Search Patterns:
* Division Problem
* Kth Object Problem

✅ https://labuladong.gitbook.io/algo/mu-lu-ye-1/mu-lu-ye-4/er-fen-fen-ge-zi-shu-zu
* Template is good, but you still need to think by yourself to adjust template for specific problem, since the f(x) changes accordingly


https://www.youtube.com/watch?v=XuwlY2p0_Ps&list=PLR6FbFmOLUglcn0VvezcLELnfSAbveoH6&index=4
Leetcode Explore: Binary Search - More Practice II

Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

"""

from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def bin_search():
            """
            Runtime: 36 ms, faster than 95.01% of Python3 online submissions for Split Array Largest Sum.
            zhijun_liao's best
            """

            def feasible(threshold: int) -> bool:
                """
                ✅ zhijun_liao: [Python] Powerful Ultimate Binary Search Template. Solved many problems
                https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems

                If you take a close look, you would probably see how similar this problem is with LC 1011 above.
                Similarly, we can design a feasible function: given an input threshold, then decide if we can split
                the array into several subarrays such that every subarray-sum is less than or equal to threshold.
                In this way, we discover the monotonicity of the problem: if feasible(m) is True, then all inputs
                larger than m can satisfy feasible function. You can see that the solution code is exactly the same as LC 1011.
                """
                # same as #806
                count, subsum = 1, 0
                for n in nums:
                    subsum += n
                    if subsum > threshold:
                        subsum = n
                        count += 1
                        if count > m:
                            return False
                return True

            vl, vr = max(nums), sum(nums)
            # https://leetcode.com/problems/split-array-largest-sum/discuss/373306/Python3-BinarySearch-Accepted-and-Well-Documented-Solution
            # XXX: What are we searching for?
            # The smallest value within this space st. we can form m (fixed)
            # subarrays from nums and none of their sums exceed that value
            while vl < vr:
                mid = (vl + vr) // 2
                # if split(mid) <= m:
                if feasible(mid):
                    # then all [mid:vr]'s feasible are True, because largest subarray sum is mid, then all value > mid makes feasible True!
                    vr = mid
                else:
                    vl = mid + 1
            return vl

        # return bf()
        return bin_search()

        """
        def split(v: int) -> int:
            # given max sum: v, what's minimum subarrays that sum < v can you form?
            # XXX: Common snippet
            count = 1
            sum = 0
            for n in nums:
                # BUG: if sum + n >= v:
                if sum + n > v:
                    # BUG: sum = 0
                    count += 1
                    sum = n
                else:
                    sum += n
            return count

        def bf():
            vl, vr = max(nums), sum(nums)
            for v in range(vl, vr + 1):
                if split(v) <= m:
                    return v
            return -1
        """


sl = Solution()
print(sl.splitArray(nums=[7, 2, 5, 10, 8], m=2))
print(sl.splitArray(nums=[1, 2, 3, 4, 5], m=2))
