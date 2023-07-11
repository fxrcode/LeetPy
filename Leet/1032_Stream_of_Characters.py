"""
Daily Challenge (Nov 30)

"""
from collections import deque
from typing import List


class TrieNode:
    def __init__(self, is_word=False) -> None:
        self.is_word = False
        self.kids = {}


class StreamChecker:
    """
    Runtime: 796 ms, faster than 53.71% of Python3 online submissions for Stream of Characters.

    AC in 10min :)
    """

    def __init__(self, words: List[str]):
        self.q = deque()
        self.root = TrieNode()

        def add(w: str):
            tail = self.root
            for c in w[::-1]:
                if c not in tail.kids:
                    tail.kids[c] = TrieNode()
                tail = tail.kids[c]
            tail.is_word = True

        for w in words:
            add(w)

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        if len(self.q) > 2000:
            self.q.popleft()

        def qry():
            tail = self.root
            for i in range(len(self.q) - 1, -1, -1):
                c = self.q[i]
                if c not in tail.kids:
                    return False
                tail = tail.kids[c]
                if tail.is_word:
                    return True
            return False

        return qry()


"""
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
"""
