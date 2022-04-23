"""
✅ GOOD Fenwick Tree
古城算法: 数据结构扩展(三) -- Binary Index Tree

https://docs.google.com/presentation/d/1yyuu0w2jJq9hLiyxAP4GiNZgOSCBb_8Ay5-usuZDi0E/edit#slide=id.gab10267339_0_71

Given: 1 <= instructions[i] <= 10^5
"""


from typing import List

MOD = int(1e9 + 7)


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        """
        Runtime: 8327 ms, faster than 15.07% of Python3 online submissions for Create Sorted Array through Instructions.

        REF: https://leetcode.com/problems/create-sorted-array-through-instructions/discuss/927531/JavaC++Python-Binary-Indexed-Tree/814904
        """
        m = max(instructions)
        bit = BIT(m + 1)
        cost = 0
        for i, n in enumerate(instructions):
            left = bit.query(n - 1)
            """ XXX: why i, rather bit.query(m)?
            The i variable in the for-loop has another meaning: the number of element before it (not include)
            Therefore, I think it is already intuitive enough that i - get(a) means to count the number of element > a.

            ow. TLE for large test case: 63 / 65 test cases passed.
            """
            right = i - bit.query(n)
            cost += min(left, right)
            bit.update(n, 1)
        return cost % MOD


class BIT:
    def __init__(self, n) -> None:
        self.ft = [0] * (n + 1)

    def update(self, x, v):
        x += 1
        while x < len(self.ft):
            self.ft[x] += v
            x += x & (-x)

    def query(self, x):
        x += 1
        ans = 0
        while x > 0:
            ans += self.ft[x]
            x -= x & (-x)
        return ans
