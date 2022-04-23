"""
tag: Medium, Hash
Lookback:
- Cool usage of `mp.setdefault(w,p)!=p`
- forward mapping: ensure no char map to 2 chars. Backward one ensures no 2 chars map to same
Similar:
- 205. Isomorphic Strings
"""

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def os_1map():
            """
            Runtime: 51 ms, faster than 39.57% of Python3 online submissions for Find and Replace Pattern.

            https://leetcode.com/problems/find-and-replace-pattern/solution/
            """

            def match(word):
                m = {}
                for w, p in zip(word, pattern):
                    if m.setdefault(w, p) != p:
                        return False
                return len(set(m.values())) == len(m.values())

            return list(filter(match, words))

        return os_1map()

        def os_2map():
            def match(word, pattern):
                m1, m2 = {}, {}
                for w, p in zip(word, pattern):
                    if w not in m1:
                        m1[w] = p
                    if p not in m2:
                        m2[p] = w
                    if (m1[w], m2[p]) != (p, w):
                        return False
                return True

            return filter(match, words)


sl = Solution()
print(sl.findAndReplacePattern(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb"))
print(sl.findAndReplacePattern(words=["a", "b", "c"], pattern="a"))
