"""
Daily Challenge (Feb 7)
tag: Easy
"""

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def os_xor():
            """
            Runtime: 48 ms, faster than 44.14% of Python3 online submissions for Find the Difference.

            """
            x = 0
            for c in s:
                x ^= ord(c)
            for c in t:
                x ^= ord(c)
            return chr(x)

        def os_hash():
            """
            Runtime: 55 ms, faster than 31.94% of Python3 online submissions for Find the Difference.
            """
            cs = Counter(s)
            for c in t:
                if c not in cs or cs[c] == 0:
                    return c
                else:
                    cs[c] -= 1

        return os_hash()


sl = Solution()
print(sl.findTheDifference("abcd", "abcde"))
print(sl.findTheDifference("", "y"))
