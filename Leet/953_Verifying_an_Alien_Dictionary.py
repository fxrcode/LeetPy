"""
FB tag
tag: easy
Lookback
- Logic! Logic! Logic!
"""

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def os():
            """
            Runtime: 32 ms, faster than 88.35% of Python3 online submissions for Verifying an Alien Dictionary.

            T:O(M)  # M: total chars in words
            """
            od = {c: i for i, c in enumerate(order)}
            for i in range(len(words) - 1):
                a, b = words[i], words[i + 1]
                for j in range(len(a)):
                    if j >= len(b):
                        return False
                    if a[j] != b[j]:
                        if od[a[j]] > od[b[j]]:
                            return False
                        break
            return True

        return os()


sl = Solution()
print(sl.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
print(
    sl.isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz")
)
