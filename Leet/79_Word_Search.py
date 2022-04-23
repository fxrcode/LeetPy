"""
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

"""


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def fxr():
            """
            Runtime: 9032 ms, faster than 8.03% of Python3 online submissions for Word Search.

            [["a"]]
            "a"

            [["a","a"]]
            "aaa"
            """
            def bt(i, j, visited, path):
                path_str = ''.join(path)
                if path_str not in hacky_trie:
                    return False
                print(i, j, visited, path)
                if path == list(word):
                    return True
                ret = False
                for dx, dy in DIR:
                    xx, yy = i+dx, j+dy
                    if not (0 <= xx < m and 0 <= yy < n) or (xx, yy) in visited:
                        continue
                    visited.add((xx, yy))
                    # XXX: OS: break instead of return directly to do some cleanup afterwards
                    ret = bt(xx, yy, visited, path+[board[xx][yy]])
                    if ret:
                        break
                    visited.remove((xx, yy))
                return ret

            '''
            def bt(r, c, visited, suffix):
                """
                REF: OS: https://leetcode.com/problems/word-search/solution/
                """
                if len(suffix) == 0:
                    return True
                if not (0 <= r < m and 0 <= c < n) or (r, c) in visited \
                        or board[r][c] != suffix[0]:
                    return False

                visited.add((r, c))
                ret = False
                for dx, dy in DIR:
                    xx, yy = r+dx, c+dy
                    ret = bt(xx, yy, visited, suffix[1:])
                    if ret:
                        break
                visited.remove((r, c))
                return ret

            '''
            hacky_trie = set([''])
            for i in range(1, len(word)+1):
                hacky_trie.add(word[:i])

            DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            m, n = len(board), len(board[0])

            for i in range(m):
                for j in range(n):
                    # if bt(i, j, set(), word):
                    if bt(i, j, set([(i, j)]), [board[i][j]]):
                        return True
            return False

        return fxr()


sl = Solution()
w = "ABCCED"
b = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# print(sl.exist(board=b, word=w))
# w = "A"
# b = [['A', 'B']]
print(sl.exist(board=b, word=w))
