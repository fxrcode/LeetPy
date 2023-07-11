"""

✅ GOOD Sliding Window
tag: Medium, Sliding Window

Lookback
- inner while => loop invariant win keep unique only, so no re-process win as I did
- contract if r-l==k!
"""

from collections import defaultdict


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        def teampark():
            """
            Runtime: 93 ms, faster than 28.61% of Python3 online submissions for Find K-Length Substrings With No Repeated Characters.

            https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/discuss/464681/Python-with-Explanation-and-Thought-Process-(Leetcode-is-Easy!)
            T: O(N)
            """
            if k > len(s):
                return 0
            freq = [0] * 26
            o = lambda c: ord(c) - ord("a")
            l, r = 0, 0
            res = 0
            while r < len(s):
                c = s[r]
                r += 1
                freq[o(c)] += 1
                while freq[o(c)] > 1:
                    d = s[l]
                    l += 1
                    freq[o(d)] -= 1
                # now windows all unique
                if r - l == k:
                    res += 1
                    # XXX: We contract our window in this step because we don't want a window that has a length GREATER than K.
                    d = s[l]
                    l += 1
                    freq[o(d)] -= 1
            return res

        return teampark()

        def fxr():
            """
            Runtime: 91 ms, faster than 30.89% of Python3 online submissions for Find K-Length Substrings With No Repeated Characters.

            T: O(N*min(m,k))
            """
            win = defaultdict(int)
            l, r = 0, 0
            ans = 0
            while r < len(s):
                c = s[r]
                r += 1
                win[c] += 1
                while r - l > k:
                    d = s[l]
                    l += 1
                    win[d] -= 1
                    if win[d] == 0:
                        del win[d]
                # now [l,r) is k size
                if r - l == k and all(v == 1 for k, v in win.items()):
                    ans += 1
            return ans

        return fxr()


sl = Solution()
print(sl.numKLenSubstrNoRepeats(s="havefunonleetcode", k=5))
print(sl.numKLenSubstrNoRepeats(s="home", k=5))
