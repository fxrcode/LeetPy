"""
✅ GOOD backtrack
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

tag: medium, backtrack
Lookback:
- How to calculate time complexity for backtrack/dfs?
    https://leetcode.com/problems/combination-sum/discuss/16634/If-asked-to-discuss-the-time-complexity-of-your-solution-what-would-you-say
    
Similar:
- Combination Sum II
"""


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def os():
            def bt(startIdx, remain, path, res):
                """
                Runtime: 64 ms, faster than 85.26% of Python3 online submissions for Combination Sum.

                XXX: OS backtrack is neat
                """
                if remain == 0:
                    res.append(path[:])
                    return
                elif remain < 0:
                    return
                for i in range(startIdx, len(candidates)):
                    c = candidates[i]
                    bt(i, remain - c, path + [c], res)

            candidates.sort(reverse=True)
            res = []
            bt(0, target, [], res)
            return res

        return os()

        def fxr():
            def bt(startIdx, remain, path, res):
                """
                Runtime: 106 ms, faster than 56.78% of Python3 online submissions for Combination Sum.

                """
                # print(startIdx, remain, path, res)
                if remain == 0:
                    res.append(path[:])
                    return
                for i in range(startIdx, len(candidates)):
                    c = candidates[i]
                    if c > remain:
                        # BUG: here i+1 then recurse, but the i in else will redo i+1!!! So duplicate!
                        bt(i + 1, remain, path, res)
                        # BUG: if you call recursion multiple times, use RETURN!!!!!!!!!!
                        # !check labuladong sudoku backtracking
                        return
                    else:
                        path.append(c)
                        bt(i, remain - c, path, res)
                        path.pop()

        return fxr()


sl = Solution()
print(sl.combinationSum(candidates=[2, 3, 5], target=8))
# print(sl.combinationSum([3, 5], 8))
# print(sl.combinationSum(candidates=[2, 3, 6, 7], target=7))
# print(sl.combinationSum([2], 1))
# print(sl.combinationSum([2], 2))
