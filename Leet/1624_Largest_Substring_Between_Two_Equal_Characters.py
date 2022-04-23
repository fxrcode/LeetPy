"""
tag: easy, hash
Lookback:
- dynamic build dict rather pre-process
- setdefault is handy: only init if key not exist and return value
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        def rock():
            """
            Runtime: 34 ms, faster than 82.20% of Python3 online submissions for Largest Substring Between Two Equal Characters.

            T: O(N). 1-pass!
            """
            ans, indices = -1, {}
            for i, c in enumerate(s):
                ans = max(ans, i - indices.setdefault(c, i) - 1)
            return ans

        return rock()

        def fxr():
            """
            Runtime: 37 ms, faster than 75.31% of Python3 online submissions for Largest Substring Between Two Equal Characters.

            T: O(2N), 2-pass!
            """
            ans = -1
            last_pos = {c: i for i, c in enumerate(s)}
            for i, c in enumerate(s):
                last = last_pos[c]
                if i != last:
                    ans = max(ans, last - i - 1)
            return ans


sl = Solution()
for s in ["aa", "abca", "cbzxy", "mgntdygtxrvxjnwksqhxuxtrv"]:
    print(sl.maxLengthBetweenEqualCharacters(s))
