"""
✅ GOOD 2ptr
✅ GOOD Sort
tag: Medium, Sort, 2ptr
Lookback:
- subseq sort is fine!
- Bad in counting (comb vs perm)
- Bad in indexing

Similar
- 2sum/3sum/4sum
- 1498. Subseq is OK to sort (CRUX)

[ ] REDO
"""

from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        def rock():
            """
            Runtime: 6105 ms, faster than 13.95% of Python3 online submissions for 3Sum With Multiplicity.

            https://leetcode.com/problems/3sum-with-multiplicity/discuss/181098/JavaPython-3-O(n2)-and-O(n-%2B-101-2)-codes-w-brief-anslysis.
            """
            arr.sort()
            ans = 0
            for i in range(2, len(arr)):
                # OS: The below is a "two sum with multiplicity".
                j, k = 0, i - 1
                while j < k:
                    sm = arr[i] + arr[j] + arr[k]
                    if sm < target:
                        j += 1
                    elif sm > target:
                        k -= 1
                    else:
                        # Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
                        # And similarly for "right".
                        l = r = 1
                        while j + l < k and arr[j] == arr[j + l]:
                            l += 1
                        while j + l < k - r and arr[k] == arr[k - r]:
                            r += 1
                        ans += (l + r) * (l + r - 1) // 2 if arr[j] == arr[k] else l * r
                        j += l
                        k -= r
            return ans % (10**9 + 7)

        return rock()

        def fxr_TLE():
            """
            TLE: 67 / 71 test cases passed.
            T: O(n^2 logn)
            """
            MOD = 10**9 + 7
            m = defaultdict(list)
            for i, n in enumerate(arr):
                m[n].append(i)

            cnt = 0
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    numk = target - arr[i] - arr[j]
                    if numk in m:
                        less = bisect_left(m[numk], x=j + 1)
                        cnt += len(m[numk]) - less
            return cnt % MOD

        return fxr_TLE()


sl = Solution()
print(sl.threeSumMulti(arr=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8))
print(sl.threeSumMulti(arr=[1, 1, 2, 2, 2, 2], target=5))
