from typing import List
# from string import ascii_letters, ascii_lowercase, ascii_uppercase


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # res = []
        # self.backtrack(s, 0, res)
        # return res

        # Iterative: Runtime: 52 ms, faster than 87.68% of Python3 online submissions for Letter Case Permutation.
        res = [s]
        for i, v in enumerate(s):
            if v.isalpha():
                res = [t[:i] + j + t[i+1:]
                       for j in (v.upper(), v.lower()) for t in res]
        return res

    def backtrack(self, s: str, start, res):
        """Recursion: beats 33% python submissions
        """
        # res (each node)
        res.append(s)

        # backtrack
        for i in range(start, len(s)):
            if s[i].isnumeric():
                continue
            # BUG: always put ternary in parantheses, ow, will get bug!
            # new_s = s[:i] + \
            #     (s[i].lower if s[i].isupper() else s[i].upper()) + s[i+1:]
            new_s = s[:i] + s[i].swapcase() + s[i+1:]
            self.backtrack(new_s, i+1, res)


sl = Solution()
s = 'a1b2'
print(sl.letterCasePermutation(s))
s = '3z4'
print(sl.letterCasePermutation(s))
s = '1234'
print(sl.letterCasePermutation(s))
