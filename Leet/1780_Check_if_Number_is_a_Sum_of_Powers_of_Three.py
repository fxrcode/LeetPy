"""

similar:
- 1774. base-3 DFS

tag: medium, math
"""


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def fxr():
            """
            Runtime: 32 ms, faster than 79.08% of Python3 online submissions for Check if Number is a Sum of Powers of Three.

            """
            x = n
            while x >= 1:
                x, q = divmod(x, 3)
                if q > 1:
                    return False
            return True

        return fxr()


sl = Solution()
for n in [12, 91, 21]:
    print(sl.checkPowersOfThree(n))
