'''
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3230/
Leetcode Explore: Array 101. Conclusion

https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming

Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.


'''


from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        def cmc():
            """
            Runtime: 382 ms, faster than 78.75% of Python3 online submissions for Max Consecutive Ones II.

            prev, cur are the consecutive 1's length (separated by last 0), note pre init to -1, means we haven't seen 0 yet!
            https://leetcode.com/problems/max-consecutive-ones-ii/discuss/96946/Concise-Python-solution-good-for-follow-up-time-O(n)-space-O(1)
            """
            pre, cur, maxlen = -1, 0, 0  # 0, 0, 0
            for n in nums:
                if n == 0:
                    pre, cur = cur, 0
                else:
                    cur += 1
                maxlen = max(maxlen, pre+1+cur)
            return maxlen

        def bf():
            """
            TLE: 12/42 test cases passed
            T: O(N^2)
            """
            max_seq = 0
            for l in range(len(nums)):
                cnt_0 = 0
                for r in range(l, len(nums)):
                    if cnt_0 > 1:
                        break
                    if nums[r] == 0:
                        cnt_0 += 1
                    if cnt_0 <= 1:
                        max_seq = max(max_seq, r-l+1)
            return max_seq

        def slide_window():
            """
            Runtime: 416 ms, faster than 54.81% of Python3 online submissions for Max Consecutive Ones II.

            AC in 1. But with hint from solution.
            """
            l, r = 0, 0
            n = len(nums)
            cnt = 0
            max_seq = 0
            while r < n:
                # expand window
                c = nums[r]
                r += 1
                if c == 0:
                    cnt += 1
                while cnt > 1:  # if window invalid: contract window
                    d = nums[l]
                    l += 1
                    if d == 0:
                        cnt -= 1
                # now cnt <= 1
                max_seq = max(max_seq, r-l)
            print(max_seq)
            return max_seq

        # return slide_window()
        return cmc()


sl = Solution()
sl.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1])
