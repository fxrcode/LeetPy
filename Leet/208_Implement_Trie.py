"""
date: 03172023
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions
"""
from collections import defaultdict


class Node:
    """
    Runtime: 188 ms, faster than 57.17% of Python3 online submissions for Implement Trie (Prefix Tree).

    """

    def __init__(self) -> None:
        self.ch = ""
        self.is_word = False
        self.children = defaultdict(Node)


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            ptr = ptr.children[c]
        ptr.is_word = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for i, ch in enumerate(word):
            if ch not in ptr.children:
                return False
            ptr = ptr.children[ch]
        return ptr.is_word

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for ch in prefix:
            if ch not in ptr.children:
                return False
            ptr = ptr.children[ch]
        return True


"""
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
"""
