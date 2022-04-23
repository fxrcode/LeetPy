"""
tag: easy, hash
Lookback:
- 1st time knew Counter +/- makes valid count (>=0)
"""

from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def pochmann():
            """
            https://stackoverflow.com/questions/21887125/adding-counters-deletes-keys
            Counter +/- will rm key if count <= 0
            """
            if len(ransomNote) > len(magazine):
                return False
            f = Counter(ransomNote) - Counter(magazine)
            print(f)
            return not f

        return pochmann()

        def fxr():
            # Runtime: 52 ms, faster than 89.80% of Python3 online submissions for Ransom Note.
            if len(ransomNote) > len(magazine):
                return False
            R, M = Counter(ransomNote), Counter(magazine)
            for k, v in R.items():
                if k not in M or M[k] < v:
                    return False
            return True


sl = Solution()
print(sl.canConstruct(ransomNote="aa", magazine="ab"))
print(sl.canConstruct(ransomNote="aa", magazine="aab"))
print(sl.canConstruct(ransomNote="aa", magazine="aaa"))
