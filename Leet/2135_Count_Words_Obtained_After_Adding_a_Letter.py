'''
Weekly Contest 275 (Jan 8, 2022)
'''
from typing import List
from string import ascii_lowercase


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def fxr():
            """
            Runtime: 2298 ms, faster than 25.00% of Python3 online submissions for Count Words Obtained After Adding a Letter.

            T: O(S)+O(T)
            """
            start = set()
            for s in startWords:
                for c in ascii_lowercase:
                    if c not in s:
                        start.add(''.join(sorted(s + c)))

            can = 0
            for t in targetWords:
                st = ''.join(sorted(t))
                if st in start:
                    can += 1
                    print(t)
            return can

        return fxr()


sl = Solution()
print(
    sl.wordCount(startWords=["ant", "act", "tack"],
                 targetWords=["tack", "act", "acti"]))

print(sl.wordCount(startWords=["ab", "a"], targetWords=["abc", "abcd"]))
