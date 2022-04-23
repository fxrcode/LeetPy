'''
✅ GOOD DP (1D) XXX: why memo is one loop, but tabulation is double loops?
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming

https://leetcode.com/problems/unique-binary-search-trees/discuss/1565493/Daily-LeetCoding-Challenge-November-Day-8
Quality problems worth doing based on Linear Dynamic Programming (1-D Dp) :
121. Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
123. Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
198. House Robber - https://leetcode.com/problems/house-robber/
279. Perfect Squares - https://leetcode.com/problems/perfect-squares/
309. Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
322. Coin Change - https://leetcode.com/problems/coin-change/
343. Integer Break - https://leetcode.com/problems/integer-break/
416. Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/
518. Coin Change 2 - https://leetcode.com/problems/coin-change-2/

Similar
95. Unique Binary Search Trees II
'''

from functools import cache


class Solution:
    def numTrees(self, n: int) -> int:
        """
        Runtime: 32 ms, faster than 59.46% of Python3 online submissions for Unique Binary Search Trees.

        XXX: os. The idea is easy. The question is: How to translate into code?
        Solution - III (Dynamic Programming - Tabulation)
        TODO: need to redo in 1 week.
        """
        def dp():
            # G[i]: numTrees with n length sequence
            G = [0]*(n+1)
            G[0] = G[1] = 1
            for i in range(2, n+1):  # with len of i nodes
                for j in range(1, i+1):  # select j as root (from node 1 to node i)
                    G[i] += G[j-1] * G[i-j]
            return G[n]
        return dp()

    def numTrees_memo(self, n: int) -> int:

        @cache
        def dp(l):
            """
            Runtime: 20 ms, faster than 99.20% of Python3 online submissions for Unique Binary Search Trees.

            https://leetcode.com/problems/unique-binary-search-trees/discuss/1565543/C%2B%2BPython-5-Easy-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Catalan-O(N)
            Solution - II (Dynamic Programming - Memoization)
            """
            if l <= 1:
                return 1
            ans = 0
            for i in range(1, l+1):
                ans += dp(i-1)*dp(l-i)
            return ans

        return dp(n)

    def numTrees_fxr(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def fxr(x):
            """
            Runtime: 28 ms, faster than 88.20% of Python3 online submissions for Unique Binary Search Trees.

            AC in 1.
            But took 30 min to tune, say
            * misled by naming param x vs n.
            * used lc+rc, rather lc*rc
            * defined 0:0 but makes lc*rc => 0, so I mathly set 0:1
            """
            # print(x, memo)
            if x in memo:
                return memo[x]
            ans = 0
            for i in range(x):
                l = i
                r = x-i-1
                # ans += fxr(l) + fxr(r)
                lc, rc = fxr(l), fxr(r)
                print('\t', l, r)
                ans += lc*rc
            memo[x] = ans
            print(x, ans)
            return ans

        return fxr(n)


sl = Solution()
print(sl.numTrees(n=4))
# print(sl.numTrees_memo(n=4))
