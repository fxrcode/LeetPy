'''
Explore Trie
tag: Medium, Trie

Lookback:
+ when prefix-str, do Trie
+ use func! rather spaghetti code!!!
'''

from typing import List
"""
class Node:
    def __init__(self) -> None:
        self.children = defaultdict(Node)
"""


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def Talse():
            """
            Runtime: 166 ms, faster than 52.92% of Python3 online submissions for Replace Words.

            REF: https://leetcode.com/problems/replace-words/discuss/105755/Python-Straightforward-with-Explanation-(Prefix-hash-Trie-solutions)/464114
            """
            def insert(s):
                p = trie
                for c in s:
                    p = p.setdefault(c, {})
                p['#'] = s

            def replace(s):
                p = trie
                for c in s:
                    # get val if key exist, ow, return None
                    p = p.get(c)
                    if not p:
                        return s
                    if '#' in p:
                        return p['#']
                return s

            trie = {}
            for root in dictionary:
                insert(root)
            print(trie)
            return ' '.join(map(replace, sentence.split()))

        return Talse()


sl = Solution()
print(
    sl.replaceWords(dictionary=["cat", "bat", "rat"],
                    sentence="c the cattle was rattled by the battery"))
print(
    sl.replaceWords(dictionary=["a", "b", "c"],
                    sentence="aadsfasf absbs bbab cadsfafs"))