"""
Tag: Medium, Greedy, Sort
Lookback:
- how to re-state/model the problem?
- how to clean code?
"""
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        def alvin777():
            prev, keep = 2e9, 0
            for freq in sorted(Counter(s).values(), reverse=True):
                freq = min(prev - 1, freq)
                if freq == 0:
                    break
                keep += freq
                prev = freq
            return len(s) - keep

        return alvin777()

        def fxr_greedy():
            nonlocal s
            s = "".join(sorted(s))
            print(s)
            cnt = Counter(s)
            freq = sorted(cnt.values(), reverse=True)
            print(freq)
            ans = 0
            for i in range(1, len(freq)):
                if freq[i] >= freq[i - 1]:
                    to = freq[i - 1] - 1
                    if to < 0:
                        to = 0
                    ans += freq[i] - to
                    freq[i] = to
            print("new: ", freq)
            return ans

        return fxr_greedy()


sl = Solution()
print(sl.minDeletions(s="aaabbbcc"))
print(sl.minDeletions(s="ceabaacb"))
print(sl.minDeletions("bbcebab"))
