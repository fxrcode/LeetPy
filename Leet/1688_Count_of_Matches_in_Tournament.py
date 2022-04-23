"""
✅ GOOD Logic
tag: easy
Lookback:
- LOGIC, LOGIC
"""


class Solution:
    def numberOfMatches(self, n: int) -> int:
        def lee215():
            # Runtime: 33 ms, faster than 76.58% of Python3 online submissions for Count of Matches in Tournament.
            return n - 1

        return lee215()

        def votrubac():
            cnt = 0
            while cnt > 1:
                cnt += n // 2
                n = (n + 1) // 2
            return cnt

        def fxr():
            """
            Runtime: 46 ms, faster than 43.97% of Python3 online submissions for Count of Matches in Tournament.

            """
            teams = n
            matches = 0
            while teams > 1:
                if teams % 2 == 1:
                    teams = (teams - 1) // 2 + 1
                    matches += teams - 1
                else:
                    teams = teams // 2
                    matches += teams
            return matches

        return fxr()


sl = Solution()
print(sl.numberOfMatches(7))
print(sl.numberOfMatches(14))
