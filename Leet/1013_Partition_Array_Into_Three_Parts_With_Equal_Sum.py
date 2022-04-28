"""
Tag: Easy
Lookback:
- partition sum: counter-part, or segment sum pre-computed
Similar:
- #1423 
"""

from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        def rock_2end():
            l, r, s = 1, len(arr) - 2, sum(arr)
            if s % 3 != 0:
                return False
            lsum, rsum, avg = arr[0], arr[-1], s // 3
            while l <= r:
                if l < r and lsum != avg:
                    lsum += arr[l]
                    l += 1
                if l < r and rsum != avg:
                    rsum += arr[r]
                    r -= 1
                if lsum == rsum == avg:
                    return True
                if l == r:
                    return False
            return False

        return rock_2end()

        def rock_count():
            # Runtime: 308 ms, faster than 97.99% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
            avg, remain, part, cnt = sum(arr) // 3, sum(arr) % 3, 0, 0
            for n in arr:
                part += n
                if part == avg:
                    cnt += 1
                    part = 0
            return remain == 0 and cnt >= 3

        return rock_count()

        def fxr_TLE():
            presum = [0]
            for n in arr:
                presum.append(presum[-1] + n)
            for l in range(len(arr) - 2):
                for r in range(l + 1, len(arr) - 1):
                    # fir: [0...l], sec: [l+1...r], third: [r+1...-1]
                    fir = presum[l + 1]
                    sec = presum[r + 1] - fir
                    third = presum[-1] - presum[r + 1]
                    if fir == sec == third:
                        return True
            return False

        return fxr_TLE()


sl = Solution()
print(sl.canThreePartsEqualSum(arr=[0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
print(sl.canThreePartsEqualSum(arr=[0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
print(sl.canThreePartsEqualSum(arr=[3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
