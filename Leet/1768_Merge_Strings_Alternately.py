"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, str
Lookback
- get familiar with lib => pythoic
- remember Python language, say for range(X) is different from C++/Java! The final i will be 1 less in python!
"""


from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def fxr():
            """
            Runtime: 41 ms, faster than 59.76% of Python3 online submissions for Merge Strings Alternately.
            """
            res = []
            for i in range(min(len(word1), len(word2))):
                res.append(word1[i] + word2[i])
            # !for i in range(5). i=4 after loop! So I need to word1[i+1:] rather word1[i:]
            res.append(word1[i + 1 :] + word2[i + 1 :])
            return "".join(res)

        return fxr()

        def lee215():
            # Runtime: 42 ms, faster than 56.79% of Python3 online submissions for Merge Strings Alternately.
            return "".join(x + y for x, y in zip_longest(word1, word2, fillvalue=""))


sl = Solution()
print(sl.mergeAlternately(word1="abc", word2="pqr"))
print(sl.mergeAlternately(word1="ab", word2="pqrs"))
print(sl.mergeAlternately(word1="abcd", word2="pq"))
