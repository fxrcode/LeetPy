"""
tag: easy
Lookback:
- life is short, use python for str process
"""


class Solution:
    def removeVowels(self, s: str) -> str:
        def fxr():
            return "".join(c for c in s if c not in "aeiou")

        return fxr()


sl = Solution()
assert (sl.removeVowels(s="leetcodeisacommunityforcoders")) == "ltcdscmmntyfrcdrs"
