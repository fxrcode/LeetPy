"""
https://leetcode.com/explore/learn/card/recursion-ii/507/beyond-recursion/2903/
Leetcode explore Recursion II: Conclusion

tag: medium, Backtracking
Lookback:
- how to convert DFS(backtrack) to @cache memoized DFS? 
    A: make it return value!
    Check 526, 131, 139.
"""

from functools import cache
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        @cache
        def memo(nums):
            """
            Runtime: 74 ms, faster than 18.60% of Python3 online submissions for Permutations.

            http://log.manl.io/cs/permutations-of-a-string-dynamic-programming-with-python/
            https://leetcode.com/problems/permutations/discuss/1722569/Python3-solution-with-memoization
            XXX: All backtrack/DFS can become @cache, just make it return res!
            inspired by 131. Palindrome Partitions.
            """
            if not nums:
                return [[]]
            res = []
            for i in range(len(nums)):
                subprob = memo(tuple(nums[:i] + nums[i + 1 :]))
                for t in subprob:
                    res.append([nums[i]] + t)
            return res

        return memo(tuple(nums))

        def fxr_9chap():
            def bt(path, visited, res):
                """
                Your runtime beats 19.07 % of python3 submissions.

                AC in 1.
                XXX: compare with 77. Combinations. That template uses start_idx, so as to pick from rest, and valid path is len(path) == k.
                    But in permutation: we use `visited`, rather `start_idx`.
                        A: because this is permute, so we can pick elem from previous index:
                        eg. we need path like: "213". So we can't use start_idx as in combinations/subsets.

                """
                # Don't put outer augment in param list if read-only!
                if len(path) == len(nums):
                    res.append(list(path))
                    return
                for n in nums:
                    if n not in visited:
                        visited.add(n)
                        bt(path + [n], visited, res)
                        visited.remove(n)

            res = []
            bt([], set(), res)
            return res


sl = Solution()
# print(sl.permute(nums=[1, 2, 3]))
# print(sl.permute(nums=list(range(8))))
sl.permute(nums=list(range(8)))
