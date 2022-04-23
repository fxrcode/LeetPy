"""
tag: Medium, presum(pre-prod), logic, Skills (indexing)
Lookback:
- Good skills, why I didn't ring the bell for preprod?
[ ] REDO
"""


class ProductOfNumbers:
    """
    Runtime: 272 ms, faster than 95.00% of Python3 online submissions for Product of the Last K Numbers.

    """

    def __init__(self) -> None:
        self.A = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.A = [1]
        else:
            self.A.append(self.A[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.A):
            return 0
        return self.A[-1] / self.A[-k - 1]


"""
class ProductOfNumbers_TLE:
    def __init__(self):
        self.q = []

    def add(self, num: int) -> None:
        self.q.append(num)

    def getProduct(self, k: int) -> int:
        res = 1
        for n in self.q[-k:]:
            res *= n
        return res
"""


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
