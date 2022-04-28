"""
Tag: Easy, String
Lookback:
- common snippet
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s


sl = Solution()
print(sl.rotateString(s="a", goal="aa"))
print(sl.rotateString(s="abcde", goal="cdeab"))
print(sl.rotateString(s="abcde", goal="abced"))
