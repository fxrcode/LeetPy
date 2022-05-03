"""
✅ GOOD string (running state + bitmask)
💡 insight
Tag: Medium, hash, bitmask, XOR, string
Lookback:
- Smart: we only care about vowel's parity, so can use bitmask 1,2,4,8,16 for 'aeiou', and use XOR to toggle odd/even.
    similar to presum, if mask[i] == mask[j], then substr[i+1...j]'s mask = 0, so even vowels!
Similar:
- 560. Subarray Sum Equals K

[ ] REDO
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def votrubac_560():
            """
            Runtime: 755 ms, faster than 38.97% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.

            T: O(N)
            """
            v = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
            mask = 0
            res = 0
            occ = [-1 for i in range(32)]
            for i, c in enumerate(s):
                if c in v:
                    mask ^= 1 << v[c]
                if mask != 0 and occ[mask] == -1:
                    occ[mask] = i
                res = max(res, i - occ[mask])
            return res

        def thejoshie_slidewin():
            """
            Runtime: 261 ms, faster than 94.12% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.

            """
            for l in range(len(s), -1, -1):
                # len(substr) = j-i+1 = l ===> j = l+i-1 < len(s) => i < len(s)-l+1
                for i in range(len(s) - l + 1):
                    sub = s[i : i + l]
                    for c in "aeiou":
                        if sub.count(c) % 2 != 0:
                            break
                    else:
                        return l

        return thejoshie_slidewin()


sl = Solution()
print(sl.findTheLongestSubstring(s="eleetminicoworoep"))
print(sl.findTheLongestSubstring(s="leetcodeisgreat"))
print(sl.findTheLongestSubstring(s="bcbcbc"))
