'''
tag: Medium, Sliding Window
'''

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def fxr():
            """
            Runtime: 265 ms, faster than 23.09% of Python3 online submissions for Find All Anagrams in a String.

            XXX: it's easier to use [0]*26 for all upper or all lower, cuz Counter[c] -= 1 will keep {c:0},
                then counter(p) = {a:1, b:1, c:1}, will not equal to win = {a:1, b:1, c:1, d:0, e:0},
            """
            o = lambda x: ord(x) - ord('a')
            # C = Counter(p)
            C = [0] * 26
            win = [0] * 26
            for c in p:
                C[o(c)] += 1
            res = []
            # win = Counter()
            l, r = 0, 0
            n = len(s)
            while r < n:
                c = s[r]
                r += 1
                win[o(c)] += 1
                while r - l > len(p):
                    d = s[l]
                    l += 1
                    win[o(d)] -= 1
                # now r - l+1 == len(p)
                if win == C:
                    res.append(l)
            return res

        def fxr_counter():
            """
            Runtime: 440 ms, faster than 13.92% of Python3 online submissions for Find All Anagrams in a String.
            """
            C = Counter(p)
            win = Counter()
            res = []
            l, r = 0, 0
            n = len(s)
            while r < n:
                c = s[r]
                r += 1
                win[c] += 1
                while r - l > len(p):
                    d = s[l]
                    l += 1
                    win[d] -= 1
                    if win[d] == 0:
                        del win[d]
                # now r - l+1 == len(p)
                if win == C:
                    res.append(l)
            return res

        return fxr_counter()


sl = Solution()
print(sl.findAnagrams(s="cbaebabacd", p="abc"))
print(sl.findAnagrams(s="abab", p="ab"))
