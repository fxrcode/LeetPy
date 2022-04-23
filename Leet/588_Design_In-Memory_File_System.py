"""
✅ GOOD Trie
tag: medium, Trie
Lookback:
- prefix => Trie (find + add), and find the major method

Weekly Special (Jan W2)
"""

from collections import defaultdict
from typing import List


class Node:
    def __init__(self) -> None:
        self.child = defaultdict(Node)
        self.content = ""


class FileSystem:
    """
    Runtime: 60 ms, faster than 55.62% of Python3 online submissions for Design In-Memory File System.
    """

    def __init__(self):
        self.root = Node()

    def _find(self, path) -> Node:  # find and return node at path
        cur = self.root
        if len(path) == 1:
            return self.root
        for w in path.split("/")[1:]:
            cur = cur.child[w]
        return cur

    def ls(self, path: str) -> List[str]:
        cur = self._find(path)
        if cur.content:  # file path, return file name
            return [path.split("/")[-1]]
        return sorted(cur.child.keys())

    def mkdir(self, path: str) -> None:
        self._find(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self._find(filePath)
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self._find(filePath)
        return cur.content


# Your FileSystem object will be instantiated and called as such:

fs = FileSystem()
print(fs.ls("/"))  # return []
fs.mkdir("/a/b/c")
fs.addContentToFile("/a/b/c/d", "hello")
print(fs.ls("/"))  # return ["a"]
print(fs.readContentFromFile("/a/b/c/d"))  # return "hello"
