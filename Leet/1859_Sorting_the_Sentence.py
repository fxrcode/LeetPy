'''
https://leetcode.com/company/google/
Easy
'''


class Solution:
    def sortSentence(self, s: str) -> str:
        """
        Runtime: 24 ms, faster than 94.99% of Python3 online submissions for Sorting the Sentence.

        AC in 2min
        """
        words = s.split(' ')
        res = [None] * len(words)

        def suffixnum(w):
            v = int(w[-1])
            prod = 1
            for i in range(len(w)-2, -1, -1):
                if not w[i].isdigit():
                    break
                prod *= 10
                v += int(w[i])*prod
            return w[:i+1], v

        for wv in words:
            w, v = suffixnum(wv)
            res[v-1] = w
        return ' '.join(res)
