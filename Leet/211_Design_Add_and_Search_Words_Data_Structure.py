"""
https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75

[ ] REDO
"""

import enum


class Node:
    def __init__(self, c='X') -> None:
        self.cha = c
        self.neighbors = dict()  # char (DOT & a~z) to Node
        self.is_word = False

    def __repr__(self) -> str:
        return self.cha


DOT = '.'
'''
class WordDictionary:
    """
    Runtime: 344 ms, faster than 54.40% of Python3 online submissions for Design Add and Search Words Data Structure.

    XXX: Don't wordy translate! There's no need ot '.' node in Trie!
    T: O(M) for well defined word, where M = key length, and N is # of keys. and O(N*26^M) for undefined words with dots.
    Worst case is word: '......' (more dots than all inserted keys)
    """
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.neighbors:
                ptr.neighbors[c] = Node(c)
            ptr = ptr.neighbors[c]
        ptr.is_word = True

    def search(self, word: str) -> bool:
        def query(cur: Node, idx):
            if idx == len(word):
                return cur.is_word
            if word[idx] == DOT:
                for c in cur.neighbors:
                    # ans |= query(cur.neighbors[c], idx+1)
                    # XXX: as in backtrack, we can quick early as soon as found match!, saved 10% runtime.
                    if query(cur.neighbors[c], idx + 1):
                        return True
            else:
                if word[idx] not in cur.neighbors:
                    return False
                return query(cur.neighbors[word[idx]], idx + 1)

        res = query(self.root, 0)
        print(word, res)
        return res
'''


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
        p['#'] = 1

    def search(self, word: str) -> bool:
        def q(s, p):
            for i, c in enumerate(s):
                if c not in p:
                    if c == '.':
                        for x in p:
                            # XXX: since it's still looking for matching, so if x = #, then ignore
                            if x != '#' and q(s[i + 1:], p[x]):
                                return True
                    return False
                else:
                    p = p[c]
            return '#' in p

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
'''
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
'''
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

wd.addWord('a')
wd.addWord('a')
# wd.search('.')
wd.addWord('ab')
print(wd.root)
# wd.search('a')
# wd.search('.a')
wd.search('a.')
