"""
✅ GOOD coding basic
FB tag (easy)

Lookback:
- sounds easy, but hard to impl neat. I like sgxu79's impl for clear logic!
- similar to basic calculator to init num/sign to generaize the logic
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        def sgxu79():
            """
            https://leetcode.com/problems/valid-word-abbreviation/discuss/1535680/Clean-Python-solution

            Runtime: 64 ms, faster than 6.49% of Python3 online submissions for Valid Word Abbreviation.
            XXX: clean & neat logic!
            """
            i, num = 0, 0
            for j, ch in enumerate(abbr):
                if ch.isdigit():
                    if num == 0 and ch == '0':
                        return False
                    num = num * 10 + int(ch)
                else:
                    i, num = i + num, 0
                    if i >= len(word) or word[i] != ch:
                        return False
                    i += 1
            return (i + num) == len(word)

        return sgxu79()
        '''
        def fxr():
            i, j = 0, 0
            k = 0
            first = True
            while i < len(abbr):
                if abbr[i].isalpha():
                    first = True
                    j = j + k
                    if j >= len(word):
                        return False
                    k = 0
                    if abbr[i] != word[j]:
                        return False
                    j += 1
                else:
                    if abbr[i] == "0" and first:
                        return False
                    k = k * 10 + int(abbr[i])
                    first = False
                i += 1
            return j + k == len(word)
        '''


sl = Solution()
print(sl.validWordAbbreviation(word="internationalization", abbr="i12iz4n"))
print(sl.validWordAbbreviation(word="apple", abbr="a2e"))
print(sl.validWordAbbreviation(word="substitution", abbr="s10n"))
print(sl.validWordAbbreviation(word="substitution", abbr="sub4u4"))
print(sl.validWordAbbreviation(word="substitution", abbr="12"))
print(sl.validWordAbbreviation(word="substitution", abbr="su3i1u2on"))
print(sl.validWordAbbreviation(word="substitution", abbr="substitution"))
print(sl.validWordAbbreviation(word="substitution", abbr="s55n"))
print(sl.validWordAbbreviation(word="substitution", abbr="s010n"))
print(sl.validWordAbbreviation(word="substitution", abbr="s0ubstitution"))
