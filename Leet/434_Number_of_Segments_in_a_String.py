"""
Tag: Easy
Lookback:
- basic skills!
"""


class Solution:
    def countSegments(self, s: str) -> int:
        def os():
            cnt = 0
            for i in range(len(s)):
                if (i == 0 or s[i - 1] == " ") and s[i] != " ":
                    cnt += 1
            return cnt

        return os()


sl = Solution()
print(sl.countSegments(s="Hello, my name is John"))
