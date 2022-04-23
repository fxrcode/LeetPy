'''
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 9: DP on String

✅ GOOD DP (LIS)

Lookback:
* Learn how to think out of box: check predessor by generation and check, so O(len(s))!
* How to REALLY use existing knowledge? Ans: 化用思想!!! rather 呆板地复制以前的代码
'''


from typing import List
from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def lee215():
            """
            Runtime: 144 ms, faster than 70.68% of Python3 online submissions for Longest String Chain.

            Time O(NlogN) for sorting,
            Time O(NSS) for the for loop, where the second S refers to the string generation and S <= 16.
            Space O(NS)
            """
            dp = {}
            words.sort(key=len)
            for w in words:
                dp[w] = max(
                    # So smart!
                    dp.get(w[:i] + w[i+1:], 0) + 1 for i in range(len(w))
                )
            return max(dp.values())

        def fxr_lis():
            """
            Runtime: 1784 ms, faster than 12.20% of Python3 online submissions for Longest String Chain.

            AC in 2nd.
            case: ["a","b","ab","bac"]

            metacognition:
            * simple variation of LIS, just need to write func to check if words[j] can become words[i] by insert 1 ch.
            """
            def is_pred(w1, w2):
                if len(w1) + 1 != len(w2):
                    return False
                i = 0
                j = 0
                diff = 0
                while i < len(w1):
                    if diff == 2:
                        break
                    if w1[i] == w2[j]:
                        i += 1
                        j += 1
                    else:
                        i += 0
                        j += 1
                        diff += 1
                print(w1, w2, diff)
                return diff <= 1

            words.sort(key=len)
            # print(words)
            T, n = defaultdict(lambda: 1), len(words)
            for i in range(1, n):
                for j in range(i):
                    if is_pred(words[j], words[i]):
                        T[i] = max(T[i], T[j]+1)
            # print(T)
            if not T:
                return 1
            return max(T.values())
        return fxr_lis()


sl = Solution()
# print(sl.longestStrChain(words=["a", "b", "ba", "bca", "bda", "bdca"]))
# print(sl.longestStrChain(words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(sl.longestStrChain(["a", "b", "ab", "bac"]))
