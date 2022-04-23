'''
Coding basic
[ ] REDO
'''


class Solution:
    def countAndSay(self, n: int) -> str:
        def dfs(n) -> str:
            """
            Runtime: 52 ms, faster than 47.97% of Python3 online submissions for Count and Say.

            T: O(N)
            """
            if n <= 1:
                return '1'
            s = dfs(n - 1)
            i, ret = 0, ''
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i + 1] == s[i]:
                    count += 1
                    i += 1
                ret += str(count) + s[i]
                i += 1
            return ret

        return dfs(n)