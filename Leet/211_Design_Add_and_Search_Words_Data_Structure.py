"""
date: 03182023
tag: Medium, Trie, DFS
https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75

[ ] REDO
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = 1

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.end_node

            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True

            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)

            return False

        return dfs(self.root, 0)


class WordDictionary:
    """
    Runtime: 308 ms, faster than 81.46% of Python3 online submissions for Design Add and Search Words Data Structure.

    REF: https://leetcode.com/problems/design-add-and-search-words-data-structure/solution/
    XXX: careful on node in traverse Trie, it's the parent of current char, especially using neat Tire {}
    """

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        p = self.root
        for c in word:
            p = p.setdefault(c, {})
        p["#"] = 1

    def search(self, word: str) -> bool:
        def q(s, p):
            for i, c in enumerate(s):
                if c not in p:
                    if c == ".":
                        for x in p:
                            # XXX: since it's still looking for matching, so if x = #, then ignore
                            if x != "#" and q(s[i + 1 :], p[x]):
                                return True
                    return False
                else:
                    p = p[c]
            return "#" in p

        res = q(word, self.root)
        # print(word, res)
        return res


'''
class WordDictionary_fxr:
    """
    TLE: 10 / 13 test cases passed.
    """
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        def aw(cur: Node, idx):
            if idx == len(word):
                cur.is_word = True
                return
            for c in [word[idx], DOT]:
                if c not in cur.neighbors:
                    cur.neighbors[c] = Node(c)
                aw(cur.neighbors[c], idx + 1)

        aw(self.root, 0)

    def search(self, word: str) -> bool:
        def qry(cur: Node, idx) -> bool:
            if idx == len(word):
                return cur.is_word
            # BUG: for c in [word[idx], DOT]:
            c = word[idx]
            if c not in cur.neighbors:
                return False
            # ans |= qry(cur.neighbors[c], idx+1)
            if qry(cur.neighbors[c], idx + 1):
                return True
            return False

        return qry(self.root, 0)
'''
"""
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
"""
wd = WordDictionary()

# wd.addWord('at')
# wd.addWord('and')
# wd.addWord('an')
# wd.addWord('add')
# wd.search('a')
# wd.search('.at')
# wd.addWord('bat')
# wd.search('.at')
# wd.search('b.')

wd.addWord("a")
wd.addWord("a")
# wd.search('.')
wd.addWord("ab")
print(wd.root)
# wd.search('a')
# wd.search('.a')
wd.search("a.")
