"""
tag: easy
Lookback:

"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        def fxr():
            """
            Runtime: 31 ms, faster than 88.77% of Python3 online submissions for Get Maximum in Generated Array.

            any math property? or simulate?

            i=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
            v=0 1 1 2 1 3 2 3 1 4 3  5  2  5  3  4
            """
            mx = 1
            if n < 2:
                return n
            V = [0, 1]
            odd = False
            for i in range(2, n + 1):
                if odd:
                    V.append(sum(V[i // 2 : i // 2 + 2]))
                else:
                    V.append(V[i // 2])
                mx = max(mx, V[-1])
                odd = not odd
            print(V)
            return mx

        return fxr()


sl = Solution()
print(sl.getMaximumGenerated(n=7))
print(sl.getMaximumGenerated(n=2))
