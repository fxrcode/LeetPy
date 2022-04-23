'''
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1137/
Leetcode Explore: Hash Table. Conclusion

The abbreviation of a word is a concatenation of its first letter, the number of characters between the first and last letter, and its last letter. If a word has only two characters, then it is an abbreviation of itself.
'''


from typing import List
from collections import defaultdict


class ValidWordAbbr:
    """
    Your runtime beats 66.13 % of python3 submissions.

    """
    @staticmethod
    def enc(s) -> str:
        if len(s) == 2:
            return s
        return s[0] + str(len(s)-2) + s[-1]

    def __init__(self, dictionary: List[str]):
        self.d = defaultdict(set)
        for s in dictionary:
            self.d[ValidWordAbbr.enc(s)].add(s)

    def isUnique(self, word: str) -> bool:
        enc_w = ValidWordAbbr.enc(word)
        if enc_w not in self.d:
            return True
        if enc_w in self.d:
            if len(self.d[enc_w]) > 1:
                return False
            return word in self.d[enc_w]
