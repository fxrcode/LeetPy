"""
Tag: Easy, Logic, Greedy
Lookback:
from 1559. 
- [ ] BOOMed by easy 2 pointer, messy logic in loop
- Greedy property proof in OS-cn
"""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        def claytonjwong():
            """
            Runtime: 199 ms, faster than 60.90% of Python3 online submissions for Assign Cookies.

            """
            g.sort()
            s.sort()
            kid, cookie = 0, 0
            while kid < len(g) and cookie < len(s):
                if g[kid] <= s[cookie]:
                    # feed the kid!
                    cookie += 1
                    kid += 1
                else:
                    # not big enough for the kid, try next cookie
                    cookie += 1
            return kid

        return claytonjwong()


sl = Solution()
print(sl.findContentChildren(g=[1, 2, 3], s=[1, 1]))
print(sl.findContentChildren(g=[1, 2], s=[1, 2, 3]))
