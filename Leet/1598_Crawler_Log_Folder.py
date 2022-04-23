"""
tag: Easy
Lookback:
"""

from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        def fxr():
            # Runtime: 62 ms, faster than 55.84% of Python3 online submissions for Crawler Log Folder.
            dep = 0
            for l in logs:
                if l.startswith("../"):
                    dep = max(0, dep - 1)
                elif l.startswith("./"):
                    continue
                else:
                    dep += 1
            return dep

        return fxr()


sl = Solution()
print(sl.minOperations(logs=["d1/", "d2/", "../", "d21/", "./"]))
print(sl.minOperations(logs=["d1/", "d2/", "./", "d3/", "../", "d31/"]))
print(sl.minOperations(["./", "wz4/", "../", "mj2/", "../", "../", "ik0/", "il7/"]))
