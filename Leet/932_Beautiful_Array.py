"""
ð¡insight
â GOOD D&C

tag: Medium, D&C, FB, math
Lookback:
- re-state problem!
    * code is easy, but logic is hard!
[ ] REDO
"""

from functools import cache
from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def yuyuyu():
            """
            Runtime: 40 ms, faster than 85.57% of Python3 online submissions for Beautiful Array.

            https://leetcode.com/problems/beautiful-array/solution/
            https://leetcode-cn.com/problems/beautiful-array/solution/932-piao-liang-shu-zu-fen-zhi-si-xiang-g-1xxg/
            XXX: æå¯¹å¤§é¨åå®æ¹é¢è§£ççæ³ï¼è¦ä¹åè­åé¿çå¾ç¨éç³æ¶ï¼è¦ä¹è¿äºç®ç­è®©äººçå¾ç¨éç³æ¶ï¼ç»è®ºï¼çå¤§é¨åå®æ¹é¢è§£å®¹æç¨éç³æ¶ã

            """

            @cache
            def dc(N):
                if N == 1:
                    return [1]
                return [2 * x - 1 for x in dc((N + 1) // 2)] + [2 * x for x in dc(N // 2)]

            return dc(n)

        return yuyuyu()

        def lee215():
            """
            https://leetcode-cn.com/problems/beautiful-array/solution/geng-xin-yi-ban-pythonde-suan-fa-jian-dan-yi-dong-/
            XXX: å ä¸ºæ¨ççæ°æ¯å¦1/2/3/4/5, 2*2=1+3, 3*2=2+4,å æ­¤ææ¨ççæ°ææ£å³å¯ã
            """

            def dc(nob_list):
                if len(nob_list) < 3:
                    return nob_list
                sub_l = dc(nob_list[::2])
                sub_r = dc(nob_list[1::2])
                return sub_l + sub_r

            n_list = list(range(1, n + 1))
            beautiful = dc(n_list)
            return beautiful

        return lee215()


sl = Solution()
print(sl.beautifulArray(n=5))
