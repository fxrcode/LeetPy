"""
https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1125/
Leetcode Explore: Hash Table. Design the Key

Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        Runtime: 28 ms, faster than 98.59% of Python3 online submissions for Group Shifted Strings.

        XXX: no need to do unicode encoding, just return tuple!
        REF: https://leetcode.com/problems/group-shifted-strings/discuss/282285/Python-Solution-with-Explanation-(44ms-84)

        """
        """
        # Runtime: 43 ms, faster than 37.45% of Python3 online submissions for Group Shifted Strings.
        def encode_fxr(s) -> str:
            # abc = bcd =xyz= 012 (means distance from ajacent chars)
            # use unicode encode so that easy to handle > 10 distance
            enc = []
            for i in range(1, len(s)):
                dif = (ord(s[i]) - ord(s[i-1])+26) % 26
                c = chr(dif + 42)
                enc.append(c)
            return ''.join(enc)
        """

        def get_hash(s):
            key = []
            for x, y in zip(s, s[1:]):
                key.append(chr((ord(y) - ord(x)) % 26 + ord("a")))
            return "".join(key)

        groups = defaultdict(list)
        for s in strings:
            hash_key = get_hash(s)
            groups[hash_key].append(s)

        return list(groups.values())


sl = Solution()
strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(sl.groupStrings(strings))
