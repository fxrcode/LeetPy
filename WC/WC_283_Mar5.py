"""
Weekly Mar 5, 2022
1st time 4/4 (AK)
But stuck in Q2 for 1hr...
"""
from bisect import bisect_left, bisect_right
from math import gcd, lcm
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        def helper(A):
            stk = []
            for i in range(len(nums)):
                while stk and gcd(stk[-1], nums[i]) > 1:
                    a = stk.pop()
                    nums[i] = lcm(a, nums[i])
                stk.append(nums[i])
            return stk

        return helper(nums)

    def createBinaryTree(self, D: List[List[int]]) -> Optional[TreeNode]:
        d = {}  # v -> node
        kid = set()
        for x in D:
            p, c, l = x
            kid.add(c)
            if c not in d:
                d[c] = TreeNode(p)
            if p not in d:
                d[p] = TreeNode(p)
            if l:
                d[p].left = d[c]
            else:
                d[p].right = d[c]
        print(d.keys)
        print(kid)
        return d[d.keys() - kid]

    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = [0] + list(set(nums))
        nums.sort()
        print(nums)
        ans = 0
        left = k

        def he(s, e):
            print(s, e)
            return (s + e) * (e - s + 1) // 2

        for x, y in zip(nums, nums[1:]):
            if left <= 0:
                break
            if y - x != 1:
                h = he(x + 1, min(y - 1, x + left))
                ans += h
                left -= min(y - 1, x + left) - (x + 1) + 1
                print(left)

        if left > 0:
            h = he(nums[-1] + 1, nums[-1] + left)
            ans += h
        return ans

    def cellsInRange(self, s: str) -> List[str]:
        c1r1, c2r2 = s.split(":")
        c1, r1 = c1r1
        c2, r2 = c2r2
        print(c1, r1)
        print(c2, r2)
        ks = range(ord(c1), ord(c2) + 1)
        rs = range(int(r1), int(r2) + 1)
        res = []
        for k in ks:
            for r in rs:
                res.append("".join([chr(k), str(r)]))
        return res


sl = Solution()
# print(sl.cellsInRange(s="K1:L2"))
# print(sl.cellsInRange(s="A1:F1"))
# print(sl.minimalKSum(nums=[5, 6], k=6))
# print(sl.minimalKSum(nums=[1, 4, 25, 10, 25], k=2))
# print(sl.minimalKSum(nums=[1, 2, 3, 4], k=2))
# print(sl.minimalKSum([96, 44, 99, 25, 61, 84, 88, 18, 19, 33, 60, 86, 52, 19, 32, 47, 35, 50, 94, 17, 29, 98, 22, 21, 72, 100, 40, 84], 35))

# print(sl.replaceNonCoprimes(nums=[6, 4, 3, 2, 7, 6, 2]))
print(sl.replaceNonCoprimes(nums=[2, 2, 1, 1, 3, 3, 3]))
