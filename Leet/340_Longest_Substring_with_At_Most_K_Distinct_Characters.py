"""
FB tag
"""

from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        def atMost():
            """
            Runtime: 149 ms, faster than 15.23% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.

            easier than lee215. 992. exact(K) = atMost(K) - atMost(K-1)
            """
            res, l, r = 0, 0, 0
            cnt = Counter()
            dst = 0
            while r < len(s):
                c = s[r]
                if cnt[c] == 0:
                    dst += 1
                cnt[c] += 1
                r += 1
                while dst > k:
                    d = s[l]
                    cnt[d] -= 1
                    if cnt[d] == 0:
                        dst -= 1
                    l += 1
                # now dst <= k
                res = max(res, r - l)
            return res

        return atMost()


sl = Solution()
print(sl.lengthOfLongestSubstringKDistinct(s="eceba", k=2))
print(sl.lengthOfLongestSubstringKDistinct(s="aa", k=1))
