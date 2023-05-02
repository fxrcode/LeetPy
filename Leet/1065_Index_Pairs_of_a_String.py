"""
✅ GOOD Trie
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

date: 05012023
tag: Easy, String, Trie
Lookback
* DON'T Explicit implement Trie!
* val = dict.setdefault(key, default)  # returns value or default!
- Pythonic

Similar:
616. Add Bold Tag in String
"""

from functools import reduce
from typing import List
from collections import defaultdict


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        def jummyEgg_pythonic():
            """
            https://leetcode.com/problems/index-pairs-of-a-string/discuss/367736/Clean-Python-Trie-Solution/467438
            """

            def Trie():
                return defaultdict(Trie)

            trie = Trie()
            for word in words:
                reduce(dict.__getitem__, word, trie)["END"] = word

            ans = []

            def dfs(text, T, start, end):
                if "END" in T:
                    ans.append([start, end - 1])
                if text and text[0] in T:
                    dfs(text[1:], T[text[0]], start, end + 1)

            for i in range(len(text)):
                dfs(text[i:], trie, i, i)

            return ans

        return jummyEgg_pythonic()

        def neat_trie():
            """
            Runtime: 40 ms, faster than 69.33% of Python3 online submissions for Index Pairs of a String.

            XXX: Don't blindly implement DS!!! This is a good example
            """

            # n - len(text)
            # m - sum(len(word))
            root, L, ans = {}, len(text), []

            def insert(s):
                p = root
                for c in s:
                    p = p.setdefault(c, {})
                p["#"] = s

            for w in words:
                insert(w)

            for i in range(L):
                p = root
                for j in range(i, L):
                    p = p.get(text[j])
                    if not p:
                        break
                    if "#" in p:
                        ans.append([i, j])
            return ans

        def pythonic():
            res = []
            for w in words:
                i = text.find(w)
                while i != -1:
                    res.append([i, i + len(w) - 1])
                    i = text.find(w, i + 1)
            return sorted(res)

        def fxr_force():
            """
            Runtime: 36 ms, faster than 89.57% of Python3 online submissions for Index Pairs of a String.


            """
            words.sort()
            lend = defaultdict(set)
            for w in words:
                lend[len(w)].add(w)
            print(lend)

            ans = []
            for l in sorted(lend.keys()):
                for i in range(len(text) - l + 1):
                    if text[i : i + l] in lend[l]:
                        ans.append([i, i + l - 1])
            ans.sort(key=lambda tu: (tu[0], tu[1]))
            return ans

        def fxr_trie():
            """
            Runtime: 136 ms, faster than 5.22% of Python3 online submissions for Index Pairs of a String.

            T:O(n*n)
            """

            class Node:
                def __init__(self) -> None:
                    self.children = {}
                    self.is_word = False

            def insert(w: str):
                p = self.root
                for c in w:
                    if c not in p.children:
                        p.children[c] = Node()
                    p = p.children[c]
                p.is_word = True

            def search(w: str):
                p = self.root
                for c in w:
                    if c not in p.children:
                        return False
                    p = p.children[c]
                return p.is_word

            self.root = Node()
            for w in words:
                insert(w)
            ans = []
            for l in range(len(text)):
                for r in range(l, len(text)):
                    if search(text[l : r + 1]):
                        ans.append([l, r])
                    # BUG: Can't early terminate in this case! Not the same as top-vote!
                    # else:
                    #     break
            return ans


sl = Solution()
print(
    sl.indexPairs(text="thestoryofleetcodeandme", words=["story", "fleet", "leetcode"])
)

assert sl.indexPairs(text="ababa", words=["aba", "ab"]) == [
    [0, 1],
    [0, 2],
    [2, 3],
    [2, 4],
]
