"""
https://leetcode.com/company/google/
Easy
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        def fxr():
            """
            Runtime: 48 ms, faster than 88.33% of Python3 online submissions for Reverse Vowels of a String.

            AC in 10min
            """
            vowels = set(list("aeiouAEIOU"))
            i, j = 0, len(s) - 1

            res = list(s)
            while i < j:
                while i < j and s[i] not in vowels:
                    i += 1
                while i < j and s[j] not in vowels:
                    j -= 1
                res[i], res[j] = res[j], res[i]
                i, j = i + 1, j - 1
            return "".join(res)

        return fxr()


sl = Solution()
print(sl.reverseVowels("hello"))
