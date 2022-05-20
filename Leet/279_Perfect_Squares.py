"""
Tag: 
Lookback:
Similar
- 322
https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/
Queue & Stack - Queue and BFS

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""
import math
import timeit
from collections import deque
from functools import cache, lru_cache
from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        """
        Runtime: 4220 ms, faster than 47.21% of Python3 online submissions for Perfect Squares.

        similar to 139. Word Break
        """
        squares = [i**2 for i in range(int(math.sqrt(n)) + 1)]
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for sqr in squares:
                if i < sqr:
                    break
                dp[i] = min(dp[i], dp[i - sqr] + 1)
        return dp[n]

    def numSquares_bfs(self, n: int) -> int:
        """[summary]
        Your runtime beats 61.78 % of python3 submissions.
        2nd rewrite BFS, got more familiar
        """
        step = 0
        q, visited = deque([n]), set([n])
        while q:
            qlen = len(q)
            for _ in range(qlen):
                cur = q.popleft()
                if cur == 0:
                    return step
                for j in range(math.isqrt(cur), 0, -1):
                    left = cur - j**2
                    if left not in visited:
                        q.append(left)
                        visited.add(left)
            step += 1
        return step

    def numSquares_DP1(self, n: int) -> int:
        """[summary]
        https://leetcode.com/problems/perfect-squares/discuss/71488/Summary-of-4-different-solutions-(BFS-DP-static-DP-and-mathematics)
        555 / 588 test cases passed. TLE: Last executed input: 2820
        """
        if n <= 0:
            return 0
        f = [0] + [4] * n
        for i in range(1, n + 1):
            for j in range(math.isqrt(n), 0, -1):
                f[i] = min(f[i], f[i - j**2] + 1)
        return f[n]

    @cache
    def numSquares_DFS_recur(self, n: int) -> int:
        """[summary]
        https://leetcode.com/problems/perfect-squares/discuss/708537/Python-recursive-solution-with-memoization-(lru_cache)
        Just tried in submission: 571 / 588 test cases passed. TLE: Last executed input: 2752
        """
        if n == 0:
            return 0
        # XXX: smart trick: if sqrt(n) is even (2k), then n = 4k^2 = (2k)^2, so return 1
        if n**0.5 % 2 == 0:
            return 1
        res = 4
        for i in range(int(n**0.5), 0, -1):
            res = min(res, self.numSquares_DFS_recur(n - i**2) + 1)
        return res

    @lru_cache(maxsize=None)
    def numSquares_DP1(self, n: int) -> int:
        """[summary]
        552 / 588 test cases passed.
        TLE for input: 7927, although I use lru_cache
        """
        if n <= 0:
            return 0
        if n**0.5 % 2 == 0:
            return 1
        minS = 4
        # BUG: for i in range(1, n), will skip for n = 1!
        # BUG: for i in range(1, n+1):
        for i in range(math.isqrt(n), 0, -1):
            # XXX: [Previous line repeated 494 more times]. If I recurse from small recur(n), it can't use overlap result.
            # So I should loop reversely, from small recur(n) to large.
            # for i in range(1, math.isqrt(n)+1):
            minS = min(minS, self.numSquares_DP1(n - i**2) + 1)
        return minS

    def numSquares_1st_BFS(self, n: int) -> int:
        """[summary]
        Runtime: 5200 ms, faster than 25.11% of Python3 online submissions for Perfect Squares.
        AC in 1st try, XXX: But took long time to get code correct. Need to practice BFS more!
        """
        """
        def sqs(n):
            res = []
            for i in range(1, 101):
                if i**2 > n:
                    break
                res.append(i)
            return res
        """

        def neighbors(n):
            res = []
            for i in range(1, n):
                if i**2 > n:
                    break
                res.append(n - i**2)
            return res

        def bfs(n):
            step = 0
            pred = {}
            q = deque([n])
            visited = set([n])
            while q:
                qlen = len(q)
                for _ in range(qlen):
                    cur = q.popleft()
                    # XXX: process cur here
                    if cur == 0:
                        return step
                    # loop level
                    for n in neighbors(cur):
                        pred[n] = cur
                        """
                        BUG: DON'T process neighbor! process cur! when pop from q!
                        if n == 0:
                            print(pred)
                            return step
                        """
                        if n not in visited:
                            q.append(n)
                            visited.add(n)
                step += 1

                """
                BUG: 0th try, not familiar to BFS template!
                for i in squares:
                    if i > cur:
                        break
                    left = cur - i
                    pred[left] = cur
                    if left in squares or left == 0:
                        print('left:', left, pred)
                        return step+1
                    # if not left in visited:
                    if left not in visited:
                        q.append(left)
                        visited.add(left)
                # finished this level
                step += 1
                """

            # after bfs, no left == 0, so not perfect squares
            return step

        return bfs(n)


sl = Solution()
for i in [12, 13, 3, 11]:  # [12]:  #
    print(sl.numSquares(i))
    print("DP:", sl.numSquares_DP_recur(i))

# XXX: how to use timeit: https://stackoverflow.com/questions/8727108/python-timeit-and-global-name-is-not-defined
print(
    timeit.timeit(
        stmt="sl.numSquares(7927)",
        setup="from __main__ import Solution; sl = Solution()",
        number=3,
    )
)
print(
    timeit.timeit(
        stmt="sl.numSquares_DP_recur(7927)",
        setup="from __main__ import Solution; sl = Solution()",
        number=3,
    )
)
print(
    timeit.timeit(
        stmt="sl.numSquares_DP2(7927)",
        setup="from __main__ import Solution; sl = Solution()",
        number=3,
    )
)
