"""
✅ GOOD Slide-window (Multi-pass)
✅ GOOD D&C
tag: medium, slide-window, D&C
Lookback:
- similar pattern: 
    - 2062: slide-window for atMost
    - 1763: D&C

[ ] REDO
"""


from collections import Counter
from functools import cache


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dbabichev_slide_window_multi_pass():
            """
            Runtime: 256 ms, faster than 23.18% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.

            T: O(26n)
            https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/949552/Python-sliding-window-solution-explained
            https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/719383/Python-O(n)-Sliding-window-Solution-based-on-template
            """

            def slide(numUniqueTarget):
                l = r = numUnique = numAtLeastK = count = 0
                freq = Counter()
                while r < len(s):
                    c = s[r]
                    if freq[c] == 0:
                        numUnique += 1
                    freq[c] += 1
                    if freq[c] == k:
                        numAtLeastK += 1
                    r += 1

                    while numUnique > numUniqueTarget:
                        d = s[l]
                        if freq[d] == k:
                            numAtLeastK -= 1
                        freq[d] -= 1
                        if freq[d] == 0:
                            numUnique -= 1
                        l += 1
                    # BUG: if numUnique == numUniqueTarget:
                    # means at most numUniqueTarget chars in window, and every freq[c] >= k
                    if numUnique == numAtLeastK:
                        count = max(count, r - l)
                return count

            mxcount = 0
            for i in range(1, len(Counter(s)) + 1):
                mxcount = max(mxcount, slide(i))
            return mxcount

        return dbabichev_slide_window_multi_pass()

        def YehudisK_1763():
            """
            Runtime: 1152 ms, faster than 12.31% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.

            https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/949688/Python-Short-and-Simple-Recursive-Solution
            """

            # @cache, no need, cuz no overlap
            def dc(s):
                if len(s) < k:
                    return ""
                freq = Counter(s)
                for i, c in enumerate(s):
                    if freq[c] < k:
                        sl = dc(s[:i])
                        sr = dc(s[i + 1 :])
                        return max(sl, sr, key=len)
                return s

            return len(dc(s))

        return YehudisK_1763()


sl = Solution()
print(sl.longestSubstring(s="aaabb", k=3))
print(sl.longestSubstring(s="ababbc", k=2))
