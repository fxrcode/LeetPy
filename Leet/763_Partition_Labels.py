"""
tag: medium, skills
Lookback:
- most problems has its own algs, need to find the logic, proof by invariant, then impl it neatly.

https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions
"""
from collections import Counter, defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def os_greedy():
            """
            Runtime: 36 ms, faster than 90.97% of Python3 online submissions for Partition Labels.

            REF: OS uses last_idx to greedy break parts
            T: O(N), M: O(26)
            """
            last_pos = {c: i for i, c in enumerate(s)}
            anchor = l = 0
            parts = []
            for r, c in enumerate(s):
                anchor = max(anchor, last_pos[c])
                if r == anchor:
                    parts.append(r - l + 1)
                    l = r + 1
            return parts

        def fxr_slidwind():
            """
            Runtime: 80 ms, faster than 10.96% of Python3 online submissions for Partition Labels.

            AC in 1. Took some time to
                * debug the matched(wind,cnt)
                * still not 100% familiar on while condition to start shrinking
            """

            def matched(wind, cnt):
                for k, v in wind.items():
                    # XXX: here's the hidden hit: once window shrink and the char removed,
                    #   it's still in wind dict, just val = 0.
                    if v == 0:
                        continue
                    if v < cnt[k]:
                        return False
                return True

            wind = defaultdict(int)
            cnt = Counter(s)
            parts = []
            l, r = 0, 0
            while r < len(s):
                c = s[r]
                r += 1
                wind[c] += 1
                # print(c, wind)

                wind_matched = matched(wind, cnt)
                first = True
                while wind_matched:
                    if first:
                        # print(wind)
                        parts.append(r - l)
                        first = False
                    d = s[l]
                    l += 1
                    wind[d] -= 1
                    if l == r:
                        wind_matched = False
            return parts

        # return fxr_slidwind()
        return os_greedy()


sl = Solution()
print(sl.partitionLabels(s="eccbbbbdec"))
print(sl.partitionLabels(s="ababcbacadefegdehijhklij"))
print(sl.partitionLabels("aabcbc"))
