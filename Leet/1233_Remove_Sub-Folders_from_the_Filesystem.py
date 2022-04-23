"""
tag: medium, Trie, Backtracking
Lookback:
- prefix / suffix => Trie
    * suffix Trie is for substr
    * prefix path, root = {} is handy, no need TrieNode
- All paths from root to leaves => Backtracking
"""

from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def rock_sort():
            # Runtime: 286 ms, faster than 80.15% of Python3 online submissions for Remove Sub-Folders from the Filesystem.
            ans = []
            for f in sorted(folder):
                if not ans or not f.startswith(ans[-1] + "/"):
                    ans.append(f)
            return ans

        def fxr():
            """
            Runtime: 301 ms, faster than 76.81% of Python3 online submissions for Remove Sub-Folders from the Filesystem.

            Wow! AC in 1 :-)
            """
            root = {}

            def insert(s):
                cur = root
                for c in s.split("/"):
                    if "#" in cur:  # early break if parent found
                        break
                    cur = cur.setdefault(c, {})
                cur["#"] = s

            # find every paths
            def bt(cur, path, res):
                if not cur or "#" in cur:
                    res.append("/".join(path))
                    return
                for c in cur:
                    bt(cur[c], path + [c], res)

            for f in folder:
                insert(f)

            res = []
            bt(root, [], res)
            return res

        return fxr()


sl = Solution()
print(sl.removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
print(sl.removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"]))
print(sl.removeSubfolders(folder=["/a/b/c", "/a/b/ca", "/a/b/d"]))
print(sl.removeSubfolders(["/a/b/c", "/a/b/c/d", "/a/b/ca", "/a/b/d"]))
