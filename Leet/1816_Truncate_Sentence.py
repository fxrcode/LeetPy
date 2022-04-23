"""
tag: easy, str
Lookback:
- neat! logic!
"""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        def fxr():
            # Runtime: 27 ms, faster than 96.06% of Python3 online submissions for Truncate Sentence.
            words = 0
            for i in range(len(s)):
                if s[i] == " ":
                    words += 1
                if words == k:
                    return s[:i]
            return s
            # return s[:i] if i < len(s) - 1 else s

        return fxr()


sl = Solution()
print(sl.truncateSentence(s="Hello how are you Contestant", k=4))
print(sl.truncateSentence(s="What is the solution to this problem", k=4))
print(sl.truncateSentence(s="chopper is not a tanuki", k=5))
