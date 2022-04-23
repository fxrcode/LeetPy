"""

古城算法: 数据结构扩展(三) -- Binary Index Tree

https://docs.google.com/presentation/d/1yyuu0w2jJq9hLiyxAP4GiNZgOSCBb_8Ay5-usuZDi0E/edit#slide=id.gab10267339_0_71
"""

from typing import List


class NumArray:
    """
    Runtime: 2677 ms, faster than 50.46% of Python3 online submissions for Range Sum Query - Mutable.

    """

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.bit = BIT(nums)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self.bit.update(index, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query(right) - self.bit.query(left - 1)


class BIT:
    def __init__(self, f) -> None:
        self.n = len(f)
        self.ft = [0] * (self.n + 1)
        for i in range(len(f)):
            self.update(i, f[i])

    def update(self, x, v):
        # XXX: careful to ++x
        x += 1
        while x < len(self.ft):
            self.ft[x] += v
            x += x & (-x)

    def query(self, x):
        # XXX: careful to ++x
        ans = 0
        x += 1
        while x > 0:
            ans += self.ft[x]
            x -= x & (-x)
        return ans


na = NumArray(nums=[1, 3, 5])
print(na.sumRange(0, 2))
na.update(1, 2)
print(na.sumRange(0, 2))

