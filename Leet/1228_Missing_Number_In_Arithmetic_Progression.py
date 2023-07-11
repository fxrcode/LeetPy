"""
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

"""


from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        def os_bisect():
            """
            Runtime: 40 ms, faster than 91.53% of Python3 online submissions for Missing Number In Arithmetic Progression.

            T: O(logN)
            """
            diff = (arr[-1] - arr[0]) // len(arr)
            # l, r = 1, len(arr)-2
            l, r = 0, len(arr) - 1
            while l < r:
                mid = (l + r) // 2
                # XXX: if curr val match with expected, then the missing must be in right side
                if arr[mid] == arr[0] + diff * mid:
                    l = mid + 1
                else:
                    r = mid
            return arr[0] + diff * l

        def fxr_brute():
            """
            Runtime: 44 ms, faster than 73.29% of Python3 online submissions for Missing Number In Arithmetic Progression.

            AC in 2.

            T: O(N)
            Edge: [0,0,0,0], should return 0
            """
            for i in range(1, len(arr) - 1):
                a, b, c = arr[i - 1 : i + 2]
                if a - b == b - c:
                    continue
                if abs(a - b) < abs(b - c):
                    return (b + c) // 2
                else:
                    return (a + b) // 2
            return arr[0]

        return os_bisect()


sl = Solution()
print(sl.missingNumber([5, 7, 11, 13]))
print(sl.missingNumber([15, 13, 12]))
print(sl.missingNumber([5, 5, 5, 5]))
print(sl.missingNumber([1, 2, 3, 5]))
