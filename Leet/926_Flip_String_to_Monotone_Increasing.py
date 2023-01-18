"""
Amazon Top50
Tag: medium
Date: 01162023
Lookback:
+ I immediately recognize it as bfs, but how to decide which bit to flip => try all => O(2^N)
+ DBabichev's init thought is DP!
"""

from collections import deque
from functools import cache


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        def os_dp():
            ans, num = 0, 0
            for c in s:
                if c == "0":
                    ans = min(num, ans + 1)
                else:
                    num += 1
            return ans

        return os_dp()

        def os_presum():
            """
            Runtime: 550 ms, faster than 21.96% of Python3 online submissions for Flip String to Monotone Increasing.

            T: O(N)
            """
            P = [0] + [0] * len(s)
            for i, c in enumerate(s):
                P[i + 1] = P[i] + int(c)

            return min(P[j] + (len(s) - j - (P[-1] - P[j])) for j in range(len(s) + 1))

        def dbabichev_dp():
            """
            REF: https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/1394780/Python-two-O(n)-solutions%3A-dp-and-accumulate-explained

            dp(i, k): on index i at the moment and we make last element (s[i]) equal to k. (k = 0 or 1)
            """
            # nonlocal s
            ss = [int(i) for i in s] + [1]

            @cache
            def dp(i, k):
                # print(i, k)
                if i == -1:
                    return 0
                return min([dp(i - 1, j) + int(k != ss[i]) for j in range(k + 1)])

            return dp(len(ss) - 1, 1)

        return dbabichev_dp()

        def fxr_bfs():
            """
            TLE: 28 / 93 test cases passed.

            my laptop time: 123.33s
            case: "0110011010001010011100011"

            1 <= s.length <= 10^5
            T: O(2^N)
            """

            def mono(s):
                o = False
                for c in s:
                    if c == "1":
                        o = True
                    else:
                        if o:
                            return False
                return True

            l = len(s)
            q = deque([s])
            seen = set([s])
            step = 0
            while q:
                qlen = len(q)
                print(qlen, len(seen))
                for _ in range(qlen):
                    cur = q.popleft()
                    if mono(cur):
                        print(cur)
                        return step
                    for i in range(l):
                        nxt = cur[:i] + str(1 - int(cur[i])) + cur[i + 1 :]
                        if nxt not in seen:
                            seen.add(nxt)
                            q.append(nxt)
                step += 1
            return -1


sl = Solution()
# s = '00110'
# s = "010110"
# s = "00011000"
s = "0110011010001010011100011"
print(sl.minFlipsMonoIncr(s))
