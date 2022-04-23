"""
✅ GOOD Roll-Hash
tag: medium, rolling-hash
Lookback:
- I learned wildcard str `ab_d` from word search (?)
- Rolling hash to check if str exists is O(1) if we need substr, better than simple set
"""

from collections import defaultdict
from sys import maxsize
from typing import List


class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        def alanlzl_rolling_hash():
            """
            Runtime: 293 ms, faster than 77.67% of Python3 online submissions for Strings Differ by One Character.
            [ ] REDO
            T: O(NM), M: O(NM)
            """
            n, m = len(dict), len(dict[0])
            hashes = [0] * n
            MOD = maxsize

            for i in range(n):
                for j in range(m):
                    hashes[i] = (26 * hashes[i] + (ord(dict[i][j]) - ord("a"))) % MOD

            base = 1
            for j in range(m - 1, -1, -1):
                seen = set()
                for i in range(n):
                    new_h = (hashes[i] - base * (ord(dict[i][j]) - ord("a"))) % MOD
                    if new_h in seen:
                        return True
                    seen.add(new_h)
                base = 26 * base % MOD
            return False

        return alanlzl_rolling_hash()

        def fxr():
            """
            Runtime: 1349 ms, faster than 8.01% of Python3 online submissions for Strings Differ by One Character.
            T:O(NM^2), M: O(NM)
            """
            m = len(dict[0])
            rm_1_char = set()
            for w in dict:
                s = list(w)
                for i in range(m):
                    s_rm1 = "".join(s[:i] + ["_"] + s[i + 1 :])
                    if s_rm1 in rm_1_char:
                        return True
                    rm_1_char.add(s_rm1)
            return False

        return fxr()


sl = Solution()
dict = ["abcd", "acbd", "aacd"]
dict = ["ab", "cd", "yz"]
dict = ["abcd", "cccc", "abyd", "abab"]
dict = ["ea", "ee", "ec", "eb"]
print(sl.differByOne(dict))
