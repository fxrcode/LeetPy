"""
✅ GOOD BFS
tag: Hard, BFS
Lookback:
- BFS: just like 1654, we need to get closer to target, not furthor!
- neat `nei(x)`: str slice `+` returns str! no need to convert to str or tuple
"""

from collections import deque


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def WangQiuc():
            """
            (optimized) Runtime: 176 ms, faster than 89.05% of Python3 online submissions for K-Similar Strings.

            Runtime: 1100 ms, faster than 11.93% of Python3 online submissions for K-Similar Strings.

            https://leetcode.com/problems/k-similar-strings/discuss/269517/Python-Graph-BFS
            XXX: get closer to target, rather move away! Choose neighbor wisely (Word XXX?)
            """

            def nei(x):
                i = 0
                while x[i] == s2[i]:
                    i += 1
                for j in range(i + 1, len(x)):
                    # if x[j] == s2[i]:
                    if x[j] == s2[i] and x[j] != s2[j]:  # (optimized)
                        yield x[:i] + x[j] + x[i + 1 : j] + x[i] + x[j + 1 :]

            q, seen = deque([(s1, 0)]), {s1}
            while q:
                x, d = q.popleft()
                if x == s2:
                    return d
                for y in nei(x):
                    if y not in seen:
                        seen.add(y)
                        q.append((y, d + 1))

        return WangQiuc()


sl = Solution()
print(sl.kSimilarity(s1="ab", s2="ba"))
print(sl.kSimilarity(s1="abc", s2="bca"))
