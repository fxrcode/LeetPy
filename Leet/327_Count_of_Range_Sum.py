"""
✅ GOOD D&C
✅ GOOD bisect
tag: Hard, D*C, bisect
Lookback:
- D&C's merge-sort application
- Som nay code pearls in each line (indexing, loop, etc), the devil is in the details

similar:
- 315

[ ] REDO
"""

from bisect import bisect_left, bisect_right, insort
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def gyh75520():
            """
            Runtime: 3695 ms, faster than 59.71% of Python3 online submissions for Count of Range Sum.

            https://leetcode.com/problems/count-of-range-sum/discuss/407655/Python-different-concise-solutions
            https://leetcode.com/problems/count-of-range-sum/discuss/77991/Short-and-simple-O(n-log-n)
            prefix-sum + merge-sort
            """
            presum = [0]
            for n in nums:
                presum.append(presum[-1] + n)

            # inclusive
            def msort(l, r):
                if l == r:
                    return 0
                mid = (l + r) // 2
                cnt = msort(l, mid) + msort(mid + 1, r)

                i = j = mid + 1
                # O(n)
                for left in presum[l : mid + 1]:
                    # find right's lower bound (i), and upper bound (j) that: right-left is in range!
                    while i <= r and presum[i] - left < lower:
                        i += 1
                    while j <= r and presum[j] - left <= upper:
                        j += 1
                    cnt += j - i

                # merge (using Timsort, so O(N))
                presum[l : r + 1] = sorted(presum[l : r + 1])
                # BUG: slicing creates NEW list! presum[l : r + 1].sort()
                return cnt

            return msort(0, len(presum) - 1)

        return gyh75520()

        def gracemeng():
            """
            TLE: 57 / 67 test cases passed.


            REF: https://leetcode.com/problems/count-of-range-sum/discuss/129018/Java-with-Explanation
            """

            def util(A: list[int]):
                count = 0
                for j in range(len(A)):
                    for i in range(1, j + 1):
                        if A[i - 1] + lower <= A[j] <= A[i - 1] + upper:
                            count += 1
                return count

            ps = [0] + [0] * len(nums)
            for i in range(len(nums)):
                ps[i + 1] = ps[i] + nums[i]

            return util(ps)

        return gracemeng()

        def kevin():
            count, s = 0, 0
            sorted_presum = [0]  # prefix sums: pre_sums[i] = sum(nums[:i])
            for x in nums:
                # s is the prefix sum of nums
                s += x

                # pre_sums[j] - pre_sums[i] = sum(nums[j:i]).
                l = bisect_left(sorted_presum, s - upper)
                r = bisect_right(sorted_presum, s - lower)

                # Count the pairs such that pre_sums[i] - pre_sums[j] is in [lower,upper].
                count += r - l

                # 把s放入排序的sorted_sums
                insort(sorted_presum, s)

            return count

        return kevin()


sl = Solution()
print(sl.countRangeSum(nums=[-2, 5, -1], lower=-2, upper=2))
# print(sl.countRangeSum([0, 0], 0, 0))
