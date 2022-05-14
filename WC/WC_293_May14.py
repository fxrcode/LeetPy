"""
May 14, 202
3/4
"""
from typing import List


class CountIntervals:

    def __init__(self):
        self.itvs = []
        self.cnt = 0
        
    def add(self, left: int, right: int) -> None:
        def overlap(i1, i2):
            if i1[1] < i2[0] or i1[0] > i2[1]:
                return False
            return True

        def merge(i1, i2):
            # assume overlap
            return [min(i1[0], i2[0]), max(i1[1], i2[1])]

        ans = []
        newInterval = [left, right]
        merged = newInterval
        for i, intv in enumerate(self.itvs):
            if overlap(intv, newInterval):
                # ans.append(merge(intv, newInterval))
                merged = merge(intv, merged)

            elif newInterval[0] > intv[1]:
                ans.append(intv)
                continue
            elif newInterval[1] < intv[0]:
                if merged:
                    ans.append(merged)
                    merged = None
                ans.extend(self.itvs[i:])
                break
        if merged:
            ans.append(merged)
        self.itvs = ans

    def count(self) -> int:

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = [0] * 32
        for c in candidates:
            for b in range(32):
                if c & (1 << b) != 0:
                    bits[b] += 1
        print(bits)
        return max(bits)

    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        p = bottom
        mx = 0
        for f in sorted(special) + [top + 1]:
            mx = max(mx, f - 1 - p + 1)
            p = f + 1
        return mx

    def removeAnagrams(self, words: List[str]) -> List[str]:
        def ana(u, v):
            u, v = list(u), list(v)
            u.sort()
            v.sort()
            return u == v

        stk = []
        for w in words:
            if stk and ana(stk[-1], w):
                continue
            stk.append(w)

        return stk


sl = Solution()
print(sl.largestCombination(candidates=[16, 17, 71, 62, 12, 24, 14]))
print(sl.largestCombination(candidates=[8, 8]))
# print(sl.maxConsecutive(bottom=2, top=9, special=[4, 6]))
# print(sl.maxConsecutive(bottom=6, top=8, special=[7, 6, 8]))
# print(sl.removeAnagrams(words=["abba", "baba", "bbaa", "cd", "cd"]))
# print(sl.removeAnagrams(words=["a", "b", "c", "d", "e"]))
