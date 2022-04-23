"""
tag: medium, greedy
Lookback:
- hiepit's generic top-down DP's reconstruct Path is good! 
- But top-down DP is not good for large input. 
- so DP -> Greedy
Similar:
- lexicographically substring/subsequence
- 1081. Smallest Subsequence of Distinct Characters
"""


from functools import cache


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        def os_greedy():
            """
            Runtime: 1579 ms, faster than 18.51% of Python3 online submissions for Smallest String With A Given Numeric Value.
            T: O(N), M: O(N)
            """
            nonlocal k
            res = [None] * n
            for i in range(n - 1, -1, -1):
                add = min(26, k - i)  # k-i: logic! so we save enough k for [:i]
                res[i] = chr(add - 1 + ord("a"))
                k -= add
            return "".join(res)

        return os_greedy()

        def fxr_2212():
            """
            TLE: 43 / 93 test cases passed. n=23100, k=567226

            same technique from 2212, but not good for large input: RecursionError: maximum recursion depth exceeded in comparison
            T: O(NK*26)
            """

            @cache
            def dp(i, w):
                print(i, w)
                if i == n:
                    return w == 0
                if w == 0:
                    return i == n
                for c in range(1, min(27, w + 1)):
                    if dp(i + 1, w - c):
                        return True
                return False

            # return dp(0, k)
            """
            technique to reconstruct DP optimal solution path from hiepit: 2212. Maximum Points in an Archery Competition
            init state to result state (the one you return, eg. i=0, w=k)
            Then loop, to see how this dp traces, use same formula in DP, remember to update states accordingly.
            """
            i, w = 0, k
            res = []
            while i < n and w > 0:
                for c in range(1, min(27, w + 1)):
                    if dp(i, w) == dp(i + 1, w - c) == True:
                        i, w = i + 1, w - c
                        res.append(chr(c - 1 + ord("a")))
                        break
            return "".join(res)

        return fxr_2212()


sl = Solution()
# print(sl.getSmallestString(n=3, k=5))
# print(sl.getSmallestString(n=3, k=27))
# print(sl.getSmallestString(n=5, k=73))
print(sl.getSmallestString(23100, 567226))
