"""
✅ GOOD Logic (Backward thinking)
tag: Medium, skills
Lookback:
- Why backward? because forward & backward logically same, but backward has neat logic
Similar:
* 452.
* 991.
"""

from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        def lee215():
            """
            Runtime: 42 ms, faster than 77.50% of Python3 online submissions for Find And Replace in String.

            XXX: backward thinking
            XXX: sorted(tuple), sort first element in tuple, if tie, break tie by next element.
            """
            nonlocal s
            for i, src, tar in sorted(zip(indices, sources, targets), reverse=True):
                s = s[:i] + tar + s[i + len(src) :] if s[i : i + len(src)] == src else s
            return s

        return lee215()

        def fxr():
            """
            Runtime: 58 ms, faster than 43.61% of Python3 online submissions for Find And Replace in String.
            T: O(nlogn)
            """
            tmp = []
            pre = 0
            mp = {idx: i for i, idx in enumerate(indices)}
            sortedindices = sorted(indices)
            for i in sortedindices:
                if not i >= pre:
                    continue
                ori = mp[i]
                src = sources[ori]
                l = len(src)
                tar = targets[ori]
                tmp.append(s[pre:i])
                if s[i : i + l] == src:
                    tmp.append(tar)
                else:
                    tmp.append(s[i : i + l])
                pre = i + l
            tmp.append(s[pre:])
            return "".join(tmp)

        return fxr()


sl = Solution()
print(sl.findReplaceString(s="abcd", indices=[0, 2], sources=["a", "cd"], targets=["eee", "ffff"]))
print(sl.findReplaceString(s="abcd", indices=[0, 2], sources=["ab", "ec"], targets=["eee", "ffff"]))
print(sl.findReplaceString("vmokgggqzp", [3, 5, 1], ["kg", "ggq", "mo"], ["s", "so", "bfr"]))
print(sl.findReplaceString("abcde", [2, 2], ["cdef", "bc"], ["f", "fe"]))
