'''
💡insight sort
tag: medium, sort

Lookback:
- taolu: sort to remove concern of one field. 
'''

from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        def os_cn_sort():
            """
            Runtime: 3625 ms, faster than 31.79% of Python3 online submissions for The Number of Weak Characters in the Game.
            
            https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game/solution/you-xi-zhong-ruo-jiao-se-de-shu-liang-by-3d2g/
            """
            properties.sort(key=lambda x: (-x[0], x[1]))
            ans = 0
            mxdef = 0
            for _, d in properties:
                if d < mxdef:
                    ans += 1
                else:
                    mxdef = d
            return ans

        def os_cn_mono():
            """
            Runtime: 2224 ms, faster than 77.99% of Python3 online submissions for The Number of Weak Characters in the Game.

            Huifeng Guan: https://www.youtube.com/watch?v=XSxnbDFz_2U
            Simple and quick analysis, no need scratchpad
            """
            properties.sort(key=lambda x: (x[0], -x[1]))
            ans = 0
            st = []
            for _, df in properties:
                while st and st[-1] < df:
                    st.pop()
                    ans += 1
                st.append(df)
            return ans

        # return os_cn_sort()
        return os_cn_mono()


sl = Solution()
properties = [[6, 9], [7, 5], [7, 9], [7, 10], [10, 4], [10, 7]]
print(sl.numberOfWeakCharacters(properties))