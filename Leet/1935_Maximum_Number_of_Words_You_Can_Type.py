"""
tag: easy
"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        def fxr():
            """
            Runtime: 41 ms, faster than 63.33% of Python3 online submissions for Maximum Number of Words You Can Type.

            T: O(NL)
            """
            bad = set(brokenLetters)
            return len([w for w in text.split() if not set(w).intersection(bad)])

        return fxr()


sl = Solution()
print(sl.canBeTypedWords(text="hello world", brokenLetters="ad"))
print(sl.canBeTypedWords(text="leet code", brokenLetters="e"))
