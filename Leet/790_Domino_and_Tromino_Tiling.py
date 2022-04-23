'''
Daily Challenge (Dec 10)

'''
from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:
        def archit91_brute():
            """
            With @cache
            Runtime: 48 ms, faster than 32.23% of Python3 online submissions for Domino and Tromino Tiling.
            T: O(N) due to each state only do one-time calc

            Without @cache
            TLE: 11 / 39 test cases passed. (n=30)
            T: O(3^N)


            WA: 13 / 39 test cases passed. (n=50)


            https://leetcode.com/problems/domino-and-tromino-tiling/discuss/1620975/C%2B%2BPython-Simple-Solution-w-Images-and-Explanation-or-Optimization-from-Brute-Force-to-DP
            DFS requires careful definition of func,state,return. Then find recurrence relation!
            """
            @cache
            def dfs(i, previous_gap):
                # base
                if i > n:
                    return 0
                if i == n:
                    if not previous_gap:
                        return 1
                    else:
                        return 0
                # recurrence
                if previous_gap:
                    return dfs(i+1, False) + dfs(i+1, True)
                return dfs(i+1, False) + dfs(i+2, False)+2*dfs(i+2, True)
            # BUG: return int(dfs(0, False) % (1e9+7)). Notice python scientific form is float, so I got wrong for some case, eg. n=50
            return dfs(0, False) % 1_000_000_007

        return archit91_brute()


sl = Solution()
print(sl.numTilings(n=30))
