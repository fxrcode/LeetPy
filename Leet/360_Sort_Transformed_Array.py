"""
✅ GOOD Logic
✅ GOOD 2ptr
tag: Medium, math, logic, 2ptr
Lookback:
- I know vertex (turning point) logic, but can't find idontknoooo's lemma
- 1st time using XOR logic in condition check, handy to use 2 cases represent 4 cases!
Similar:
- 977
"""

from bisect import bisect_left
from typing import List


class Solution:
    def sortTransformedArray(
        self, nums: List[int], a: int, b: int, c: int
    ) -> List[int]:
        def idontknoooo():
            """
            Runtime: 61 ms, faster than 51.25% of Python3 online submissions for Sort Transformed Array.
            https://leetcode.com/problems/sort-transformed-array/discuss/83331/Python-O(n)-Two-Pointers-Solution/250513
            https://leetcode.com/problems/sort-transformed-array/discuss/766072/Python-3-or-Math-%2B-Two-Pointer-or-Detailed-explanation-with-ascii-drawing
            lemma from vertex:
                When a>0, the largest number is either on left or right end of nums.

                Correspondingly,
                When a<0, the smallest number is either on left or right end of nums.
            """

            def calc(x):
                return a * x * x + b * x + c

            n = len(nums)
            l, r, ans = 0, n - 1
            ans = []
            while l <= r:
                l_val, r_val = calc(nums[l]), calc(nums[r])
                """
                XXX: how to find this? simply draw the table=> when to append(l_val)?
                append(l_val): (<,<) or (>,>)
                append(r_val): (<,>) or (>,<)
                Q: How to bool represent these 4?
                Ans: xy+x̄ȳ = x^ȳ (x means a>0, y means nums[left]<nums[right]).
                It comes from x^y = xȳ + x̄y
                """
                if (a > 0) ^ (l_val < r_val):
                    ans.append(l_val)
                    l += 1
                else:
                    ans.append(r_val)
                    r -= 1
            return ans if a <= 0 else ans[::-1]

            # if a >= 0:
            #     if l_val > r_val:
            #         ans[idx] = l_val
            #         l += 1
            #     else:
            #         ans[idx] = r_val
            #         r -= 1
            #     idx -= 1
            # else:
            #     if l_val > r_val:
            #         ans[idx] = r_val
            #         r -= 1
            #     else:
            #         ans[idx] = l_val
            #         l += 1
            #     idx += 1

        return idontknoooo()

        def fxr():
            """
            Runtime: 88 ms, faster than 8.24% of Python3 online submissions for Sort Transformed Array.

            """

            def calc(x):
                return a * x**2 + b * x + c

            def shuxue():
                if a == 0:
                    return nums
                turn = -b / 2 / a

                idx = bisect_left(nums, turn)
                print(turn, idx)
                if idx <= 0 or idx >= len(nums):
                    return nums
                l, r = idx - 1, idx
                res = []
                while l >= 0 and r < len(nums):
                    if abs(nums[l] - turn) < abs(nums[r] - turn):
                        res.append(nums[l])
                        l -= 1
                    else:
                        res.append(nums[r])
                        r += 1
                print(l, r)
                res.extend(nums[: l + 1][::-1] if l >= 0 else nums[r:])
                return res

            return list(map(calc, shuxue()))

        return fxr()


sl = Solution()
print(sl.sortTransformedArray(nums=[-4, -2, 2, 4], a=1, b=3, c=5))
print(sl.sortTransformedArray(nums=[-4, -2, 2, 4], a=-1, b=3, c=5))
