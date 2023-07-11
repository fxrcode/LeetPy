"""
✅ GOOD Math (Modulo)
Daily Challenge (Jan 2)

"""
from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        def os_modula():
            """
            Runtime: 354 ms, faster than 12.02% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.

            (a+b)%c <=> ((a%c) + (b%c)) % c!
            so (a+b)%60 = 0 <=>
                case 1: both a,b mod 60 = 0
                case 2: (a%60) + (b%60) = 60
            """
            remainders = defaultdict(int)
            ans = 0
            for t in time:
                if t % 60 == 0:
                    ans += remainders[0]
                else:
                    ans += remainders[60 - t % 60]
                # XXX: only update dict with me after calculating rather precompute!
                remainders[t % 60] += 1
            return ans

        def fxr_hash():
            """
            Runtime: 528 ms, faster than 5.02% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.

            T: O(N * 1000//60) # cuz time in [1,500]
            """
            cntr = defaultdict(int)
            for t in time:
                cntr[t] += 1

            sixties = [i * 60 for i in range(500 * 2 // 60 + 1)]
            pairs = 0
            for t in time:
                for sixty in sixties:
                    if t >= sixty:
                        continue
                    if sixty == 2 * t:
                        p = cntr[t] - 1
                        if p > 0:
                            print("\t", sixty, p, t)
                        pairs += p
                    else:
                        p = cntr[sixty - t]
                        if p > 0:
                            print(sixty, p, t)
                        pairs += p
            return pairs // 2

        return fxr_hash()


sl = Solution()
print(sl.numPairsDivisibleBy60(time=[30, 20, 150, 100, 40]))
print(sl.numPairsDivisibleBy60(time=[60, 60, 60]))
print(sl.numPairsDivisibleBy60([15, 63, 451, 213, 37, 209, 343, 319]))
