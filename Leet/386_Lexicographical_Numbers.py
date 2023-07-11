"""

✅ GOOD DFS, iteration
Kevin

tag: medium, DFS
Lookback:
- Polya 1st: understand the problem!
- Learn a complex enough but not too complex example, as GeorgeChryso plot
"""

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def hack_sort():
            """
            Runtime: 116 ms, faster than 80.34% of Python3 online submissions for Lexicographical Numbers.

            https://leetcode-cn.com/problems/lexicographical-numbers/solution/jian-dan-pai-xu-by-qian-li-ma-8-vjjr/
            T: O(nlogn)
            """
            lst = [i for i in range(1, n + 1)]
            return sorted(lst, key=lambda x: str(x))

        def hzb_iter():
            """
            Runtime: 238 ms, faster than 31.62% of Python3 online submissions for Lexicographical Numbers.

            https://leetcode-cn.com/problems/lexicographical-numbers/solution/386-zi-dian-xu-pai-shu-o1-kong-jian-fu-z-aea2/
            T: O(N), T: O(1)
            """
            ans = []
            v = 1
            while len(ans) < n:
                while v <= n:
                    ans.append(v)
                    v *= 10
                while v % 10 == 9 or v > n:
                    v //= 10
                v += 1
            return ans

        return hzb_iter()

        def hzb_dfs():
            """
            https://leetcode-cn.com/problems/lexicographical-numbers/solution/386-zi-dian-xu-pai-shu-o1-kong-jian-fu-z-aea2/
            """

            def dfs(x):
                if x > n:
                    return
                res.append(x)
                for nxt in range(x * 10, x * 10 + 10):
                    dfs(nxt)

            res = []
            for x in range(1, 10):
                dfs(x)
            return res

        def GeorgeChryso():
            """
            Runtime: 118 ms, faster than 77.77% of Python3 online submissions for Lexicographical Numbers.

            https://leetcode.com/problems/lexicographical-numbers/discuss/399796/EasyandSimple-recursion-beats-100-!-Explanation-%2B-Graphic-Illustration-Included
            T: O(N)
            """
            res = []

            def dfs(start, end):
                while start <= end and start <= n:
                    res.append(start)
                    dfs(start * 10, start * 10 + 9)
                    start += 1

            dfs(1, 9)
            return res


sl = Solution()
print(sl.lexicalOrder(n=112))
