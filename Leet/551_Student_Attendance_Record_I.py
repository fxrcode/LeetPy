"""
tag: easy
Lookback:
- TODO: 1-pass
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        def fxr():
            """
            Runtime: 38 ms, faster than 67.33% of Python3 online submissions for Student Attendance Record I.

            """
            return s.count("A") < 2 and s.find("LLL") == -1
