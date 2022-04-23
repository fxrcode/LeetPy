"""

What's Trie?
- A trie is a n-ary tree that stores strings.
- Each trie node represents a string (a prefix).
- Each node might have several children nodes, while the `paths` to different children nodes represent `different chars`.
- linear time to search a str.
- same time but less space compare to HashTable.

When use Trie?
- prefix-str, string match
- suffix: find substr

REF: https://leetcode.com/problems/replace-words/discuss/105755/Python-Straightforward-with-Explanation-(Prefix-hash-Trie-solutions)/464114

Example
648. Replace Words
1065. Index Pairs of a String
616. Add Bold Tag in String
1268. Search Suggestions System
1698. Number of Distinct Substrings in a String
1233. Remove Sub-Folders from the Filesystem

"""

from collections import defaultdict
from typing import List


# classic textbook impl is crystal clear
class Node:
    def __init__(self):
        self.kids = defaultdict(Node)
        # here should have a isend attribute, we store the word instead.
        self.word = None


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.kids[c]
        cur.word = word

    def find(self, word):
        cur = self.root
        for c in word:
            # this means this sentence word has no 'root'
            if c not in cur.kids:
                return word
            cur = cur.kids[c]
            if cur.word is not None:
                return cur.word
        # cannot find a matched root for current word
        return word


class TrieNeat:
    """
    # 758: https://leetcode.com/problems/bold-words-in-string/discuss/247076/Optimized-Python-Solution-using-Trie-Tree-and-Merge-Intervals
    neat impl, no need of TrieNode
    """

    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.setdefault(c, {})
        cur["#"] = word

    def find(self, word):
        cur = self.root
        for i in word:
            cur = cur[i]
            if not cur:
                return word
            if "#" in cur:
                return cur["#"]
        return word


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        roots = Trie()
        for word in dict:
            roots.insert(word)
        return " ".join(roots.find(word) for word in sentence.split())
