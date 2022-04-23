"""
CS 106B
"""


class Backtrack:
    @staticmethod
    def permute(s: str) -> list[str]:
        def bt(s, visited, path, res):
            if len(path) == len(s):
                res.append(''.join(path))
                return
            for i in range(len(s)):
                c = s[i]
                # simple dedup: recursive dup by order, requires s sorted
                if i > 0 and s[i] == s[i-1] and i-1 not in visited:
                    continue
                if i not in visited:
                    visited.add(i)
                    path.append(c)
                    bt(s, visited, path, res)
                    # XXX: if forgot unchoose, then only one str in res! cuz all i in visited by left most bt()
                    path.pop()
                    visited.remove(i)
        res = []
        bt(s, set(), [], res)
        return res

    @staticmethod
    def subsets(A: list[int]) -> list[list[int]]:
        """
        Q: What's the backtrack different from permutation's decision. A: combination cares include/exclude, rather order!
        XXX: here I used 9chap's backtrack combination template, rather 106B's include vs exclude.
        """
        def bt(A, start, path, res):
            # BUG: if start >= len(A): every node is valid solution!
            res.append(path[:])
            for i in range(start, len(A)):
                bt(A, i+1, path+[A[i]], res)
                # BUG: bt(A, i+1, path, res)
        res = []
        bt(A, 0, [], res)
        return res

    @ staticmethod
    def escape_maze(M: list[list[int]]):
        pass


# print(Backtrack.permute("abc"))
# print(Backtrack.permute("abcc"))
print(Backtrack.subsets([1, 2, 3]))
