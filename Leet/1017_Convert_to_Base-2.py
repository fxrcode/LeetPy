'''
✅ GOOD Logic
tag: Math, Medium
[ ] REDO
'''


class Solution:
    def baseNeg2(self, n: int) -> str:
        def lee215():
            """
            Runtime: 56 ms, faster than 12.00% of Python3 online submissions for Convert to Base -2.

            """
            res = []
            x = n
            while x:
                res.append(x & 1)
                x = -(x >> 1)
            return ''.join(map(str, res[::-1] or [0]))

        return lee215()


sl = Solution()
for n in [2, 3, 4, 10]:
    print(sl.baseNeg2(n))