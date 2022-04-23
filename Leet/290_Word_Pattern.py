'''
Daily Challenge (Jan 17)
This problem is similar to Isomorphic Strings.
'''

from typing import List
from collections import defaultdict
from itertools import zip_longest


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def os_mapindex():
            """
            Use only single map: key/word first occurence
            OS has good case walk through

            T: O(N)
            """
            map_index = {}
            words = s.split()
            if len(pattern) != len(words):
                return False
            for i, w in enumerate(words):
                c = pattern[i]
                char_key = f'char_{c}'
                char_word = f'word_{w}'
                if char_key not in map_index:
                    map_index[char_key] = i
                if char_word not in map_index:
                    map_index[char_word] = i
                if map_index[char_key] != map_index[char_word]:
                    return False
            return True

        return os_mapindex()

        def fxr():
            """
            Runtime: 45 ms, faster than 23.29% of Python3 online submissions for Word Pattern.

            T: O(N), M:O(2N)
            """
            p2s, s2p = defaultdict(str), defaultdict(str)
            if len(pattern) != len(s.split()):
                return False
            for a, b in zip(pattern, s.split()):
                c = p2s[a]
                d = s2p[b]
                if c == d == '':
                    p2s[a] = b
                    s2p[b] = a
                elif c != b or d != a:
                    return False
            return True


sl = Solution()
print(sl.wordPattern(pattern="abba", s="dog cat cat dog"))
print(sl.wordPattern(pattern="abba", s="dog cat cat fish"))
print(sl.wordPattern(pattern="aaaa", s="dog cat cat dog"))
print(sl.wordPattern("aaa", "aa aa aa aa"))
print(sl.wordPattern("he", "unit"))
