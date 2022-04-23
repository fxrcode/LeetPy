"""
✅ GOOD BFS (bi-directional)
Tag: Medium, BFS
Lookback:
- bi-directional BFS (expand smaller q)
- How to prune?
Similar:
- Frog jump, Knight Tour, Open Lock, Word Ladder
"""

from collections import deque
from string import ascii_lowercase
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def agave_preprocess_bfs():
            """
            https://leetcode.com/problems/word-ladder/discuss/40723/Simple-to-understand-Python-solution-using-list-preprocessing-and-BFS-beats-95
            """

            def construct_dict(word_list):
                d = {}
                for word in word_list:
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i + 1 :]
                        d[s] = d.get(s, []) + [word]
                return d

            def bfs_words(begin, end, dict_words):
                queue, visited = deque([(begin, 1)]), set()
                while queue:
                    word, steps = queue.popleft()
                    if word not in visited:
                        visited.add(word)
                        if word == end:
                            return steps
                        for i in range(len(word)):
                            s = word[:i] + "_" + word[i + 1 :]
                            neigh_words = dict_words.get(s, [])
                            for neigh in neigh_words:
                                if neigh not in visited:
                                    queue.append((neigh, steps + 1))
                return 0

            d = construct_dict(wordList | set([beginWord, endWord]))
            return bfs_words(beginWord, endWord, d)

        # return agave_preprocess_bfs()

        def dasheng2_bi_bfs():
            """
            Runtime: 112 ms, faster than 95.63% of Python3 online submissions for Word Ladder.

            https://leetcode.com/problems/word-ladder/discuss/40710/Share-my-two-Python-solutions%3A-a-very-concise-one-(12-lines-~160ms)-and-an-optimized-solution(~100ms)
            Bi-directional BFS (if end is given!)
            """
            l = 2
            q1, q2 = set([beginWord]), set([endWord])
            wordDict = set(wordList)
            wordDict.discard(beginWord)
            if endWord not in wordDict:
                return 0
            while q1:
                # generate all valid transform (aka goto neighbor)
                q1 = wordDict & (
                    set(
                        word[:i] + ch + word[i + 1 :]
                        for word in q1
                        for i in range(len(beginWord))
                        for ch in ascii_lowercase
                    )
                )
                if q1 & q2:
                    return l
                l += 1
                # XXX: search from the side with fewer nodes
                if len(q1) > len(q2):
                    q1, q2 = q2, q1
                # remove transforms from wordDict to avoid cycle
                wordDict -= q1
            return 0

        def fxr_bfs():
            """
            Runtime: 774 ms, faster than 15.16% of Python3 online submissions for Word Ladder.

            """

            dict = set(wordList)
            # bfs
            q = deque([beginWord])
            seen = set([beginWord])
            levels = 0

            while q:
                qlen = len(q)
                for _ in range(qlen):
                    cur = q.popleft()
                    if cur == endWord:
                        return levels
                    for i in range(len(cur)):
                        c = cur[i]
                        for d in ascii_lowercase:
                            if d == c:
                                continue
                            nxt = cur[:i] + d + cur[i + 1 :]
                            if nxt not in dict or nxt in seen:
                                continue

                            q.append(nxt)
                            seen.add(nxt)
                levels += 1
            return 0
