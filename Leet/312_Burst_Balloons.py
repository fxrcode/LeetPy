"""
✅ GOOD DP (formula design)
Tag: Medium, DP
Lookback:
- [ ] REDO

Daily Challenge (Jan 1)

https://leetcode.com/problems/burst-balloons/discuss/970727/Python-5-lines-dp-explained
Similar:
664 Strange Printer
546 Remove Boxes
1000 Minimum Cost to Merge Stones
"""

from functools import cache
from typing import List


class Solution:
    def maxCoins(self, N: List[int]) -> int:
        def dbabichev_topdown():
            """
            Runtime: 9904 ms, faster than 44.87% of Python3 online submissions for Burst Balloons.

            T: O(n^3)
            """
            A = [1] + N + [1]

            @cache
            def dfs(l, r):
                if l > r:
                    return 0
                ans = 0
                for i in range(l, r + 1):
                    # i-th balloon is the last to burst!
                    gain = A[l - 1] * A[i] * A[r + 1]
                    remain = dfs(l, i - 1) + dfs(i + 1, r)
                    ans = max(ans, gain + remain)
                return ans

            return dfs(1, len(A) - 2)

        def fxr_bf():
            """
            TLE: [35,16,83,87,84,59,48,41,20,54]

            T: O(N!)
            """

            def lr(i):
                lv, rv = 1, 1
                for l in range(i - 1, -1, -1):
                    if N[l] != -1:
                        lv = N[l]
                        break
                for r in range(i + 1, len(N)):
                    if N[r] != -1:
                        rv = N[r]
                        break
                return (lv, rv)

            def bf(left, coins, gain):
                if left == 0:
                    gain.append(coins)
                    return
                for i in range(len(N)):
                    if N[i] == -1:
                        continue

                    l, r = lr(i)
                    ori = N[i]
                    N[i] = -1
                    bf(left - 1, coins + l * ori * r, gain)
                    N[i] = ori

            gain = []
            bf(len(N), 0, gain)
            print(sorted(gain))
            return max(gain)

        # return fxr_bf()
        return dbabichev_topdown()


sl = Solution()
print(sl.maxCoins(N=[3, 1, 5, 8]))
