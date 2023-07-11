"""
✅ GOOD Logic
logic: re-state, rather simulation!
similar in Stefan's interval merge

Amazon tag
tag: easy, 2ptr

Lookback
- UNDERSTAND problem, then restart it.
"""
from collections import defaultdict


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        def os_groupby():
            """
            Runtime: 208 ms, faster than 46.70% of Python3 online submissions for Count Binary Substrings.

            T: O(N), M: O(N)
            """
            groups = [1]
            for i in range(1, len(s)):
                if s[i - 1] != s[i]:
                    groups.append(1)
                else:
                    groups[-1] += 1

            ans = 0
            for i in range(1, len(groups)):
                ans += min(groups[i - 1], groups[i])
            return ans

        def os_groupby_optimize():
            """
            prev, cur <=> groups[-2], groups[-1]
            T: O(N), M:O(1)
            """
            ans, prev, cur = 0, 0, 1
            for i in range(1, len(s)):
                if s[i - 1] != s[i]:
                    ans += min(prev, cur)
                    prev, cur = cur, 1
                else:
                    cur += 1
            return ans + min(prev, cur)

        return os_groupby_optimize()


sl = Solution()
print(sl.countBinarySubstrings(s="00110011"))
print(sl.countBinarySubstrings(s="10101"))
