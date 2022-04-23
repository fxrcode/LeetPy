"""
✅ GOOD Sort (cyclic-sort)
tag: easy, sort, skills
Lookback:
- Why Cyclic Sort? Because it's put number into position!
- Clear thought on indexing

Similar:
41.
268.
1920.
"""

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        def cyclic_sort():
            """
            Runtime: 65 ms, faster than 72.40% of Python3 online submissions for Shuffle String.

            https://leetcode.com/problems/shuffle-string/discuss/755923/Used-Cyclic-Sort-with-O(1)-SPACE-and-O(N)-Time-complexity
            M: O(1)

            """

            def swap(A, i, j):
                A[i], A[j] = A[j], A[i]

            ss = list(s)
            for i in range(len(s)):
                while indices[i] != i:
                    swap(ss, i, indices[i])
                    swap(indices, i, indices[i])
                    """
                    ss[indices[i]], ss[i] = ss[i], ss[indices[i]]
                    #! bug of Python
                    indices[i], indices[indices[i]] = indices[indices[i]], indices[i]
                    """
            return "".join(ss)

        return cyclic_sort()

        def fxr():
            # Runtime: 85 ms, faster than 43.70% of Python3 online submissions for Shuffle String.
            # res = s
            # res = [] * len(s)
            res = list(s)
            for i, c in zip(indices, s):
                res[i] = c
            return "".join(res)


sl = Solution()
print(sl.restoreString(s="code", indices=[3, 0, 1, 2]))
