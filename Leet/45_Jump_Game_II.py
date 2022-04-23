'''
✅ GOOD BFG (model as graph)

https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming


'''


from typing import List


class Solution:

    def jump_Neet(self, nums: List[int]) -> int:
        """
        XXX: Neet's BFS analysis is easier than OS's greedy
        Runtime: 120 ms, faster than 90.77% of Python3 online submissions for Jump Game II.

        REF: https://www.youtube.com/watch?v=dJ7sWiOoK7g
        """
        ans = 0
        l = r = 0
        while r < len(nums)-1:
            farthest = 0
            for j in range(l, r+1):
                farthest = max(farthest, j+nums[j])
            l = r+1
            r = farthest
            ans += 1
        return ans

    def jump_backtrack(self, nums: List[int]) -> int:
        """
        TLE: 73 / 106 test cases passed.

        REF: https://leetcode.com/problems/jump-game/discuss/1443541/Python-2-approaches%3A-Top-down-DP-Max-Pos-So-Far-Clean-and-Concise
        1st attempt, learned the loop sage from hiepit's 55. Jump Game
        """
        N = len(nums)
        INF = 1e6

        def rec(i):
            if i == N-1:
                return 0
            ans = INF
            for j in range(i+1, min(i+nums[i], N-1) + 1):
                # BUG: ans = min(ans, rec(j)) + 1
                ans = min(ans, rec(j))
            return ans + 1

        return rec(0)
        # for i in range(N):
        #     print(i, rec(i))


def WRONG():
    nums = [1, 2, 1, 0]
    ans = 100
    for n in nums:
        # BUG: don't add during staging for minimum
        ans = min(ans, n)+1
        print(n, ans)
    print(ans)


# WRONG()


sl = Solution()
print(sl.jump(nums=[2, 3, 1, 1, 4]))
print(sl.jump(nums=[2, 3, 0, 1, 4]))

# XXX: lead to TLE if using backtracking. Check Neet's recursion tree
print(sl.jump([5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9,
               6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5]))
