from collections import Counter
from heapq import heappop, heappush
from random import randint
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        def heapq():
            minh = []
            for n in nums:
                heappush(minh, n)
                if len(minh) > k:
                    heappop(minh)
            C = Counter(minh)
            ans = []
            for n in nums:
                if C[n] > 0:
                    C[n] -= 1
                ans.append(n)
            return ans

        def fxr_sort():
            """
            Runtime: 86 ms, faster than 26.64% of Python3 online submissions for Find Subsequence of Length K With the Largest Sum.

            T: O(nlogn)
            """
            n = sorted(list((x, i) for i, x in enumerate(nums)))
            n = n[-k:]
            n = sorted(list((i, x) for x, i in n))
            n = list(x for _, x in n)
            return n

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def fxr_qselect():
            """
            Runtime: 128 ms, faster than 7.69% of Python3 online submissions for Find Subsequence of Length K With the Largest Sum.

            T: O(N), M: O(N)
            """

            def partition(b, e):
                r = randint(b, e)
                swap(r, e)
                p = nums[e]

                l = b - 1
                for i in range(b, e):
                    if -nums[i] < -p:
                        l += 1
                        swap(l, i)
                swap(l + 1, e)
                return l + 1

            def qselect():
                l, r = 0, len(nums) - 1
                while l < r:
                    mid = partition(l, r)
                    if mid == k:
                        break
                    elif mid < k:
                        l = mid + 1
                    else:
                        r = mid

            numscopy = nums[:]
            qselect()
            ans = []
            C = Counter(nums[:k])
            for n in numscopy:
                if C[n] > 0:
                    C[n] -= 1
                    ans.append(n)
            return ans

        return fxr_qselect()


sl = Solution()
# print(sl.maxSubsequence(nums=[2, 1, 3, 3], k=2))
print(sl.maxSubsequence(nums=[-1, -2, 3, 4], k=3))
