"""
✅ GOOD Stack (mono-stack)
Amazon Top50
tag: medium, mono-stack
Lookback:
- 1588 for combination maths & 84 for mono-stack logic!
"""

from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def justin_yuan_histogram_rectangle():
            """
            Runtime: 456 ms, faster than 97.52% of Python3 online submissions for Sum of Subarray Minimums.

            https://leetcode-cn.com/problems/sum-of-subarray-minimums/solution/python3-tong-84ti-zui-da-zhi-fang-tu-by-5ersw/
            Awesome graph!
            """
            A = arr + [-1]
            stk, res = [-1], 0
            for i, v in enumerate(A):
                while stk and A[stk[-1]] > A[i]:
                    idx = stk.pop()
                    H = A[idx]
                    W = (i - idx) * (idx - stk[-1])
                    res += H * W
                stk.append(i)
            return res % (10**9 + 7)

        return justin_yuan_histogram_rectangle()

        def cindyzhou_mono_incr():
            """
            https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170776/Python-Simple-Stack-O(n)-Solution-10-lines
            T: O(N)
            """
            res = 0
            stk = []
            A = [float("-inf")] + arr + [float("-inf")]
            for i, n in enumerate(A):
                while stk and A[stk[-1]] > n:
                    cur = stk.pop()
                    res += A[cur] * ((i - cur) * (cur - stk[-1]))
                stk.append(i)
            return res % (10**9 + 7)


sl = Solution()
arr = [3, 1, 2, 4]
print(sl.sumSubarrayMins(arr))
