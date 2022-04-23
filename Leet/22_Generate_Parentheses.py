'''
https://leetcode.com/explore/learn/card/recursion-ii/503/recursion-to-iteration/2772/
Leetcode explore Recursion II: Recursion to Iteration
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

'''


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Your runtime beats 71.27 % of python3 submissions.

        XXX: Labuladong ch 4.3: Backtracking example.
        Based upon backtracking template, just modify to constrain by valid paranthesis check.
        """
        def bt(left, right, track, res):
            if right < 0 or left < 0:
                return
            if left > right:
                return
            if left == right == 0:
                res.append(''.join(track))
                return

            track.append('(')
            bt(left-1, right, track, res)
            track.pop()

            track.append(')')
            bt(left, right-1, track, res)
            track.pop()

        res = []
        bt(n, n, [], res)
        return res

    '''
    def generateParenthesis_fxr_WRONG(self, n: int) -> List[str]:
        """
        BUG: my 1st attempt, not fully understand backtrack!
        """
        def bt(n, i, path, seen, res):
            if i == n:
                res.append(path[:])
                return
            for p in path:
                for cand in ['('+p+')', '()'+p, p+'()']:
                    if cand in seen:
                        continue
                    path.append(cand)
                    seen.add(cand)
                    bt(n, i+1, path, seen, res)
                    seen.remove(cand)
                    path.pop()

        res = []
        bt(n, 0, [''], set(), res)
        return res
    '''


sl = Solution()
print(sl.generateParenthesis(3))
