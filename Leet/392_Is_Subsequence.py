"""
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, 
    and you want to check one by one to see if t has its subsequence. 
    In this scenario, how would you change your code?

Lookback:
- subsequence: MIT subproblem trick dp(i,j) prefer suffix.
    * However, 2ptr to be linear is the best.
- followup is always interesting. Binary search!
"""


from bisect import bisect_left
from collections import defaultdict
from functools import cache


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def dbabichev_2ptr():
            """
            Runtime: 35 ms, faster than 81.46% of Python3 online submissions for Is Subsequence.
            T: O(m+n)
            """
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i, j = i + 1, j + 1
                else:
                    j += 1
            return i == len(s)

        return dbabichev_2ptr()

        def follow_up_dbabichev():
            """
            !GEM: bisect_left for cur_place in c2i[c], so we make sure we can find c in c2i[c] >= cur_place
            https://leetcode.com/problems/is-subsequence/discuss/678389/Python-3-Solutions%3A-DP-2-pointers-and-follow-up-BS-explained
            T: O(mlogn)
            """
            c2i = defaultdict(list)
            for c, i in enumerate(t):
                c2i[c].append(i)

            cur_place = 0
            for c in s:
                cur_idx = bisect_left(c2i[c], x=cur_place)
                if cur_idx >= len(c2i[c]):
                    return False
                cur_place = c2i[c][cur_idx] + 1
            return True

        def topdown_dp():
            """
            Runtime: 70 ms, faster than 12.33% of Python3 online submissions for Is Subsequence.
            !MIT DP I: LCS

            T: O(mn)
            """
            slen, tlen = len(s), len(t)

            @cache
            def dp(i, j):
                if i == slen:
                    return True
                if j == tlen:
                    return False
                if s[i] == t[j]:
                    return dp(i + 1, j + 1)
                else:
                    return dp(i, j + 1)
                    # return dp(i + 1, j) or dp(i, j + 1)

        def os_dp():
            """
            XXX: This is simplified "Edit distance" with only deletion
            The OS's draw of 2D and whole DP tabulation illustration is good
            """
            sl, tl = len(s), len(t)
            if sl == 0:
                return True
            # XXX: sl x tl, according to the 2D, commonly make n+1 for string DP, to handle '' empty prefix, so simplified if/else.
            # F[r][c] = maximal subsequence from s[:r], t[:c]
            F = [[0] * (tl + 1) for _ in range(sl + 1)]
            for c in range(1, tl + 1):
                for r in range(1, sl + 1):
                    if s[r - 1] == t[c - 1]:
                        F[r][c] = F[r - 1][c - 1] + 1
                    else:
                        F[r][c] = max(F[r][c - 1], F[r - 1][c])
                if F[sl][c] == sl:
                    return True
            return False

        def fxr_brute():
            """
            Runtime: 28 ms, faster than 90.66% of Python3 online submissions for Is Subsequence.

            AC in 1.
            T: O(m+n)
            """
            i, j = 0, 0  # pointer for s,t
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == len(s)

        """
        def fxr_WA():
            # BUG: subsequence/string has order!!!
            cnt = Counter(t)
            cnts = Counter(s)
            for k, v in cnts.items():
                if k not in cnt or cnt[k] < v:
                    return False
            return True
        """

        # return fxr_WA()
        return os_dp()


sl = Solution()
print(sl.isSubsequence(s="abc", t="ahbgdc"))
print(sl.isSubsequence(s="axc", t="ahbgdc"))
print(sl.isSubsequence(s="acb", t="ahbgdc"))
