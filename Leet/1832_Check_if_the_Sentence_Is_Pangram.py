"""
Facebook tag

tag: Easy, bit manipulation, hash

Lookback:
- when you see limited state => bit manipulation (eg. DFS w/ bitmask)
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        def sachuverma():
            """
            Runtime: 58 ms, faster than 12.58% of Python3 online submissions for Check if the Sentence Is Pangram.

            https://leetcode.com/problems/check-if-the-sentence-is-pangram/discuss/1164135/Simple-solution-no-setmap/910621
            M: O(1)
            """
            tmp, need = 0, (1 << 26) - 1
            for c in sentence:
                tmp |= 1 << (ord(c) - ord("a"))
                if tmp == need:
                    return True
            return tmp == need

        return sachuverma()

        def fxr():
            """
            Runtime: 40 ms, faster than 46.06% of Python3 online submissions for Check if the Sentence Is Pangram.

            T: O(L) # L = all alphabeta in sentence
            """
            seen = set(sentence)
            return len(seen) == 26


sl = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
sentence = "leetcode"
print(sl.checkIfPangram(sentence))
