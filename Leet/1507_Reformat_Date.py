'''
tag: easy

Lookback:
- Python str not familiar
'''


class Solution:
    def reformatDate(self, date: str) -> str:
        def leihao1313():
            """
            Runtime: 28 ms, faster than 91.12% of Python3 online submissions for Reformat Date.

            """
            M = [
                "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
                "Oct", "Nov", "Dec"
            ]
            d, m, y = date.split()
            return f'{y}-{(M.index(m)+1):02d}-{int(d[:-2]):02d}'