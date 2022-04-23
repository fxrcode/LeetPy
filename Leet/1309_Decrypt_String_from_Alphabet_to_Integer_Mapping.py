"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, skills
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        def fxr():
            """
            Runtime: 50 ms, faster than 39.02% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.

            """
            res = []
            i = len(s) - 1
            while i >= 0:
                if s[i] == "#":
                    c = chr(int(s[i - 2 : i]) - 10 + ord("j"))
                    res.append(c)
                    i -= 3
                else:
                    c = chr(int(s[i]) - 1 + ord("a"))
                    res.append(c)
                    i -= 1
            return "".join(res[::-1])

        return fxr()


sl = Solution()

print(sl.freqAlphabets(s="10#11#12"))
print(sl.freqAlphabets(s="1326#"))
