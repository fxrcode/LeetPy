"""
Tag: Easy
Lookback:
- rather simulate, we can find the complement, so as to O(nd)
"""

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def cutequokka():
            # Runtime: 309 ms, faster than 56.48% of Python3 online submissions for Count the Number of Consistent Strings.
            al = set(allowed)
            cnt = 0
            for w in words:
                for c in w:
                    if c not in al:
                        cnt += 1
                        break
            return len(words) - cnt

        def fxr():
            al = set(allowed)
            # res = []
            cnt = 0
            for w in words:
                if set(w) <= al:
                    cnt += 1
            return cnt

        return fxr()


sl = Solution()
print(sl.countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]))
print(sl.countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]))
print(sl.countConsistentStrings(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))
