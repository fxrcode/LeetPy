"""
✅ GOOD Math (Group Theory)
tag: Medium, Array, Math
Lookback:
- rotate image
- cyclic swap (in-place)
- reminds me #1654: Minimum jumps to reach home (Bezout Theorem)
Similar:
- 1260

Leetcode Explore Array & String: Conclusion
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1182/

"""


from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def os3_cyclic_swap():
            """
            Runtime: 594 ms, faster than 20.78% of Python3 online submissions for Rotate Array.

            Group Theory: Group Action, orbit-stabilizer theorem
            https://leetcode.com/problems/rotate-array/solution/205266
            """
            nonlocal k
            """
            def gcd(a, b):
                # XXX: no order required. 3%7 = 3 ===> 3=0*7+3.
                while b:
                    a, b = b, a % b
                return a
            """

            n = len(nums)
            k %= n

            start_idx = count = 0
            while count < n:
                cur_idx, tmp = start_idx, nums[start_idx]
                while True:
                    nxt_idx = (cur_idx + k) % n
                    nums[nxt_idx], tmp = tmp, nums[nxt_idx]
                    cur_idx = nxt_idx
                    count += 1

                    if start_idx == cur_idx:
                        break
                start_idx += 1

            print(nums)

        return os3_cyclic_swap()

        def os4_rev():
            """
            Runtime: 232 ms, faster than 55.03% of Python3 online submissions for Rotate Array.
            XXX: find patterns! <The Art and Craft of Problem Solving (3/e)>. or Neetcode
            or like playing sudoku
            """
            n = len(nums)
            k %= n

            def rev(nums, l, r):
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1

            rev(nums, 0, n - k - 1)
            rev(nums, n - k - 1 + 1, n - 1)
            rev(nums, 0, n - 1)
            return nums

        def fxr_simulate():
            """
            Do not return anything, modify nums in-place instead.
            """
            n = len(nums)
            res = [0] * n
            for i in range(n):
                print(nums[i], i, (i + k) % n)
                res[(i + k) % n] = nums[i]

            return res


sl = Solution()
print(sl.rotate([1, 2, 3, 4, 5, 6, 7], 3))
