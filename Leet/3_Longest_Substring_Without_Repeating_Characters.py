"""
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1135/
Leetcode Explore: Hash Table. Conclusion
Given a string s, find the length of the longest substring without repeating characters.

"""


from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Your runtime beats 50.09 % of python3 submissions.

        AC in 2nd submission after debugging. Still buggy in sliding window:
        1) what does inner while do?
        2) what does window maintain? index? count?
        3) does window <=> [l,r)
        """
        wind = defaultdict(int)  # char: count
        best = 0
        ans = ""
        l, r = 0, 0  # [l,r)
        while r < len(s):
            c = s[r]
            r += 1
            wind[c] += 1
            # to make window valid, pop left
            while wind[c] != 1:
                d = s[l]
                l += 1
                # BUG:  if d == c: wind[d] -= 1
                # ! Wtf did I add d== c to decr wind counter ?!
                wind[d] -= 1
            # now wind is valid: wihtout repeating chars
            # update best, ans
            if best < r - l:
                best = r - l
                ans = s[l:r]
        return best, ans


sl = Solution()
print(sl.lengthOfLongestSubstring("abcabcbb"))
print(sl.lengthOfLongestSubstring("tmmzuxt"))
