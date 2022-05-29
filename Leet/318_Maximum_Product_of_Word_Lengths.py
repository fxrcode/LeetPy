"""
Tag: Medium, bitmask
Lookback:
- Yedelm: Bitmask is a great trick when dealing with some string related problem and only care about presence of characters. It's not used that often but worth to know it.
"""

from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def hiepit_bitmask():
            """
            T: O(N^2 + L), where N is number of words, L is total length of words.
            """
            n = len(words)
            bm = [0] * n
            for i in range(n):
                for c in words[i]:
                    bm[i] |= 1 << (ord(c) - ord("a"))

            ans = 0
            for i in range(n):
                for j in range(i + 1, n):
                    if (bm[i] & bm[j]) == 0:
                        ans = max(ans, len(words[i]) * len(words[j]))
            return ans

        def fxr():
            """
            Runtime: 513 ms, faster than 80.22% of Python3 online submissions for Maximum Product of Word Lengths.

            """
            mx = 0
            ws = [set(w) for w in words]
            for i in range(len(words)):
                for j in range(i + 1, len(words)):
                    if ws[i].isdisjoint(ws[j]):
                        print(words[i], words[j])
                        mx = max(mx, len(words[i]) * len(words[j]))
            return mx

        return fxr()


sl = Solution()
print(
    sl.maxProduct(
        ["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"]
    )
)
print(sl.maxProduct(words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
print(sl.maxProduct(words=["a", "aa", "aaa", "aaaa"]))
