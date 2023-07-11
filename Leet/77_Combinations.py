"""
https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2798/
Leetcode explore Recursion II: Backtracking

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
"""


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Your runtime beats 71.68 % of python3 submissions.
        AC in 1.

        XXX: This is combination backtrack template. For combination/subset, we can skip choice[i] in path!
            and valid solution just by len(path)

        Compare with 46. Permutations/17. Phone letter combinations.
        """

        def bt(start_idx, path, res):
            if len(path) == k:
                res.append(list(path))
                return

            for i in range(start_idx, n):
                path.append(i + 1)
                bt(i + 1, path, res)
                path.pop()

        res = []
        bt(0, [], res)
        return res


sl = Solution()
print(sl.combine(n=4, k=2))
print(sl.combine(n=1, k=1))
