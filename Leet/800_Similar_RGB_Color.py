"""
Tag: Easy, Sort, Math
Lookback:
- 00,11,22,..., ee. Can be calculated in k*16+k for k in range(1,16)
- 1st time using hex()[2:].zill(2)
- neat === modular
"""


class Solution:
    def similarRGB(self, color: str) -> str:
        def ye15():
            """
            Runtime: 32 ms, faster than 91.80% of Python3 online submissions for Similar RGB Color.

            https://leetcode.com/problems/similar-rgb-color/discuss/119845/Simple-python-solution/840688
            """

            def f(c):
                ans = 0
                for k in range(1, 16):
                    ans = min(ans, k * 16 + k, key=lambda x: abs(x - int(c, 16)))
                return hex(ans)[2:].zfill(2)

            return "#" + "".join(f(color[i : i + 2]) for i in (1, 3, 5))

        return ye15()


sl = Solution()
print(sl.similarRGB("#09f166"))
print(sl.similarRGB("#4e3fe1"))
