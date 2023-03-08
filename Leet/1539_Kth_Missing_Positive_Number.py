"""
date: 03052023
✅ GOOD Bisect (hat)
    k-th xxx (max/min/freq) in set => Given constant val, search if exists subset that count(<=val) >= k.
✅ GOOD logic
💡insight
tag: Easy, Bisect, Google
Lookback:
- similar compare logic: 581.
- What's diff from 41? (cyclic sort?)

Here are some similar binary search problems.
Also find more explanations.
Good luck and have fun.

1539. Kth Missing Positive Number
1482. Minimum Number of Days to Make m Bouquets
1283. Find the Smallest Divisor Given a Threshold
1231. Divide Chocolate
1011. Capacity To Ship Packages In N Days
875. Koko Eating Bananas
774. Minimize Max Distance to Gas Station
410. Split Array Largest Sum
"""

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def os_bisect():
            """
            Runtime: 48 ms, faster than 85.32% of Python3 online submissions for Kth Missing Positive Number.

            We need a way to check on how many positive integers are missing before the given array element to use binary search. To do that, let's compare the input array [2, 3, 4, 7, 11] with an array with no missing integers: [1, 2, 3, 4, 5]. The number of missing integers is a simple difference between the corresponding elements of these two arrays:
            * arr=[2,3,4,7,11], origin=[1,2,3,4,5]
                Before 2, there is 2 - 1 = 1 missing integer.
                Before 3, there is 3 - 2 = 1 missing integer.
                Before 4, there is 4 - 3 = 1 missing integer.
                Before 7, there are 7 - 4 = 3 missing integers.
                Before 11, there are 11 - 5 = 6 missing integers.

            why l+k: We use binary search to find the smallest index, l, such that there are more than k missing numbers in [0, A[l]].
            The actual number of missing numbers in [0, A[l-1]] is A[l-1] - (l - 1) - 1 = A[l-1] - l.
            Counting from A[l-1], The k-th missing number is therefore A[l-1] + k - (A[l-1] - l) = l + k

            XXX: careful on l,r!!! they're defined by problem's specific search space! You need to fully check problem so as to get l,r right!
                not simply 0, len(arr)-1! ow. failed for certain case: eg. [1,2,3,4], k=2
                check: https://leetcode.com/problems/kth-missing-positive-number/discuss/780201/Java-O(lgN)-binary-Search
            """
            # l, r = 0, len(arr)-1
            l, r = 0, len(arr)
            while l < r:
                m = (l + r) // 2
                if arr[m] - (m + 1) >= k:
                    r = m
                else:
                    l = m + 1
            print(l, r)
            return l + k

        return os_bisect()

        def os_brute():
            """
            Runtime: 52 ms, faster than 65.00% of Python3 online submissions for Kth Missing Positive Number.

            XXX: learned many pearl of coding basics, logic
            T: O(N)
            """
            nonlocal k
            if k <= arr[0] - 1:
                return k
            k -= arr[0] - 1

            # search kth missing between the arr numbers
            for i in range(len(arr) - 1):
                # missing between arr[i] and arr[i+1]
                cur_missing = arr[i + 1] - arr[i] - 1
                # if the kth missing in this gap
                # XXX: It's <=, rather <. Ow. Will fail at case: arr=[1,3], k=1
                if k <= cur_missing:
                    return arr[i] + k
                k -= cur_missing
            # if missing number is greater than arr[-1]
            return arr[-1] + k

        def fxr_brute():
            """
            Runtime: 52 ms, faster than 65.00% of Python3 online submissions for Kth Missing Positive Number.

            AC in 10min
            T: O(N)
            """
            miss = 0
            i, j = 1, 0
            while j < len(arr) and miss < k:
                if i == arr[j]:
                    i, j = i + 1, j + 1
                else:
                    miss += 1
                    i += 1
            return i + k - miss - 1


sl = Solution()
print(sl.findKthPositive(arr=[2, 3, 4, 7, 11], k=5))
