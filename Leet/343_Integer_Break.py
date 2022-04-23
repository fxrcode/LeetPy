'''
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 14: Classic Dynamic Programming Problems
'''
import timeit
from functools import cache


class Solution:
    def integerBreak(self, n: int) -> int:
        def theflyingemini_dp():
            """
            https://leetcode.com/problems/integer-break/discuss/484055/RZ-O(n-2)-DP-solution-and-O(n)-solution-based-on-math
            Runtime: 28 ms, faster than 90.97% of Python3 online submissions for Integer Break.
            """
            f = [0]*(n+1)
            f[1] = 1
            for i in range(2, n+1):
                for j in range(1, i//2+1):
                    tmp = max(j, f[j]) * max(i-j, f[i-j])
                    f[i] = max(f[i], tmp)
            return f[n]

        def theflyingemini_math():
            """
            O(N)

            """
            nonlocal n
            if n == 2:
                return 1
            if n == 3:
                return 2

            res = 1
            while n > 4:
                res *= 3
                n -= 3
            return res * n

        def hydro_bird():
            """
            Runtime: 24 ms, faster than 97.00% of Python3 online submissions for Integer Break.

            https://leetcode.com/problems/integer-break/discuss/80689/A-simple-explanation-of-the-math-part-and-a-O(n)-solution/173495

            O(logN)
            """
            nonlocal n
            if n <= 3:
                return n-1
            num_3 = n//3
            rem = n % 3
            if rem == 1:
                rem = 4
                num_3 -= 1
            elif rem == 0:
                rem = 1
            return pow(3, num_3) * rem

        def fxr_dp_WA():
            """
            only need factors 2 or 3, and as much 3's as possible.

            """
            @cache
            def twothree(i):
                if i <= 3:
                    return i-1
                if i == 4:
                    return 4
                return max(twothree(i-2)*2, twothree(i-3)*3)
            return twothree(n)

        def fxr_backtrack():
            """
            TLE: n >= 42

            Metacognition: it's like subset backtracking, so use startIdx to prevent duplicate enumerate,
            so mine is better than hiepit_backtrack. But I stuck in subset backtrack template!
            Still not fully grasp backtrack! Need more practice and review!

            """
            ans = [0]

            def bt(start, n, prod, k, ans):
                # print(start, n, prod, k)
                # print(locals())
                # base
                if n == 0:
                    if k >= 2:
                        ans[0] = max(ans[0], prod)
                # recur
                for i in range(start, n+1):
                    bt(i, n-i, prod*i, k+1, ans)

            bt(1, n, 1, 0, ans)
            return ans[0]

        def hiepit_backtrack():
            # TLE if n >= 25
            ans = [0]

            def bt(n, product, k):
                print
                # base
                if n == 0 and k >= 2:
                    ans[0] = max(ans[0], product)
                    return
                # recur
                for i in range(1, n+1):
                    bt(n-i, product*i, k+1)

            bt(n, 1, 0)
            return ans[0]

        # return hiepit_backtrack()
        # return fxr_backtrack()
        # return theflyingemini_dp()
        return theflyingemini_math()


sl = Solution()
for i in range(2, 15):
    print(i, sl.integerBreak(i))
# print(sl.integerBreak(n=58))
# print(timeit.timeit(stmt='sl.integerBreak(n=25)',
#                     setup='from __main__ import Solution; sl = Solution()', number=1))
