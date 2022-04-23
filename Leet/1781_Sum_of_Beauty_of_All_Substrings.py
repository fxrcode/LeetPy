"""
tag: Medium, 2ptr
Lookback:
- slide-window template (const len)
"""

from collections import Counter


class Solution:
    def beautySum(self, s: str) -> int:
        def lenchen1112_slide_win():
            """
            Runtime: 4870 ms, faster than 53.75% of Python3 online submissions for Sum of Beauty of All Substrings.

            """
            beauty, n = 0, len(s)
            for l in range(3, n + 1):
                cnt = Counter()
                for j in range(l):
                    cnt[s[j]] += 1
                beauty += max(cnt.values()) - min(cnt.values())
                for j in range(l, n):
                    cnt[s[j]] += 1
                    cnt[s[j - l]] -= 1
                    if cnt[s[j - l]] == 0:
                        del cnt[s[j - l]]
                    beauty += max(cnt.values()) - min(cnt.values())
            return beauty

        return lenchen1112_slide_win()

        def fxr():
            # Runtime: 4448 ms, faster than 58.93% of Python3 online submissions for Sum of Beauty of All Substrings.
            n = len(s)
            ans = 0

            def beauty(f):
                return max(f.values()) - min(f.values())

            for i in range(n):
                freq = Counter()
                for j in range(i, n):
                    freq[s[j]] += 1
                    ans += beauty(freq)
            return ans

        return fxr()


sl = Solution()
print(sl.beautySum(s="aabcb"))
print(sl.beautySum(s="aabcbaa"))
