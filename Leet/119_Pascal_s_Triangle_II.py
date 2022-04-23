"""
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming

https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1171/
Leetcode Explore Array & String: Conclusion

tag: easy, DP
lookback
- learn how to iterative DP (order!)
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def iter_tsao(rowIndex):
            """[summary]
            Runtime: 28 ms, faster than 89.31% of Python3 online submissions for Pascal's Triangle II.

            AntaresTsao: use trick of zip(a,b), so as to mimic prev[i], prev[i+1]
            https://leetcode.com/problems/pascals-triangle-ii/discuss/38467/Very-simple-Python-solution
            """
            res = [1]

            for _ in range(rowIndex):
                res = [x + y for x, y in zip([0] + res, res + [0])]
            return res

        def iter_girikuncoro(rowIndex):
            """[summary]
            https://leetcode.com/problems/pascals-triangle-ii/discuss/38574/Simple-Python-5-lines-36ms
            """
            pasal = [1] * (rowIndex + 1)
            for i in range(2, rowIndex + 1):
                for j in range(i - 1, 0, -1):
                    pasal[j] += pasal[j - 1]
                print(pasal)
            return pasal

        # print("iter_girikuncoro", iter_girikuncoro(rowIndex))
        # return iter_tsao(rowIndex)
        return iter_girikuncoro(rowIndex)

    def getRow_R(self, rowIndex: int) -> List[int]:
        def recur(rowIndex: int) -> List[int]:
            """
            Your runtime beats 99.21 % of python3 submissions.

            Basic recursive solution, with trick from Neetcode
            https://www.youtube.com/watch?v=nPVEaB3AjUM&list=UU_mYaQAE6-71rjSN6CeCA-g&index=23
            """
            if rowIndex == 0:
                return [1]

            prev = [0] + recur(rowIndex - 1) + [0]
            res = []
            for i in range(rowIndex + 1):
                res.append(prev[i] + prev[i + 1])

            return res

        return recur(rowIndex)


sl = Solution()
print(sl.getRow(10))
