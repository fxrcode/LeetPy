"""
Tag:
Similar:
Lookback:
- first 🔥 [LeetCode The Hard Way] 🔥 Explained Line By Line, and her logic, code, comments are quite good template to follow
"""

from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        def lthw():
            """
            https://leetcode.com/problems/find-duplicate-file-in-system/discuss/2595019/LeetCode-The-Hard-Way-Explained-Line-By-Line
            takeaway: more cleaner
            """
            m = defaultdict(list)
            for p in paths:
                # 1. split the string by ' '
                path = p.split()
                # the first string is the directory path
                # the rest of them are just file names with content
                directoryPath, rest = path[0], path[1:]
                # for each file names with content
                for f in rest:
                    # we retrieve the file name and the file content
                    fileName, fileContent = f.split("(")[0], f.split("(")[1][:-1]
                    # then group {directoryPath}/{fileName} by file content
                    m[fileContent].append("{}/{}".format(directoryPath, fileName))
            # return the file list only when the size is greater than 1, meaning they are duplicate files
            return [m[k] for k in m.keys() if len(m[k]) > 1]

        def fxr_hash_parse():
            v2p = defaultdict(list)
            res = []
            for l in paths:
                tmp = l.split()
                p, fs = tmp[0], tmp[1:]
                for f in fs:
                    ftmp = f.split("(")
                    fn, fv = ftmp[0], str(ftmp[1][:-1])
                    # print(f"{fn=}, {fv=}")
                    v2p[fv].append(f"{p}/{fn}")
            # print(v2p)
            for p in v2p.values():
                if len(p) > 1:
                    res.append(p)
            return res

        return lthw()


sl = Solution()
paths0 = [
    "root/a 1.txt(abcd) 2.txt(efsfgh)",
    "root/c 3.txt(abdfcd)",
    "root/c/d 4.txt(efggdfh)",
]
paths1 = [
    "root/a 1.txt(abcd) 2.txt(efgh)",
    "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)",
    "root 4.txt(efgh)",
]
paths2 = [
    "root/a 1.txt(abcd) 2.txt(efgh)",
    "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)",
]
print(sl.findDuplicate(paths=paths1))
