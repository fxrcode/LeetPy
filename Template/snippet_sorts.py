"""
+ Quicksort/select in K-th largest item

+ Mergesort: 315, 315. Count of Smaller Numbers After Self
"""

from random import randint


class Solution:
    def quick_sort(self, A, start, end):
        """Hoare 2way partition of quicksort"""
        if start >= end:
            return

        left, right = start, end
        pivot = A[(start + end) // 2]
        # partition template
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        # after partition, [right, left] are adjacent
        self.quick_sort(A, start, right)
        self.quick_sort(A, left, end)

    def quick_sort_lomuto(self, A, start, end):
        """lomuto partition version of quicksort"""
        if start >= end:
            return

        # choose a pivot element A[p]
        pi = self.lomuto(A, start, end)

        self.quick_sort_lomuto(A, start, pi - 1)
        self.quick_sort_lomuto(A, pi + 1, end)

    def lomuto(self, A, start, end):
        # swap end to randint, so p is randomized
        Solution.swap(A, randint(start, end), end)
        p = end
        l = start - 1
        for i in range(start, end):
            if A[i] < A[p]:
                l = l + 1
                Solution.swap(A, i, l)
        Solution.swap(A, l + 1, p)
        return l + 1

    def qselect(self, A, lo, hi, k):
        if lo >= hi:
            return A[lo]
        pi = self.lomuto(A, lo, hi)
        if pi == k:
            return A[k]
        elif pi < k:
            return self.qselect(A, pi + 1, hi, k)
        else:
            return self.qselect(A, lo, pi - 1, k)

    @staticmethod
    def swap(A, i, j):
        A[i], A[j] = A[j], A[i]

    @staticmethod
    def dutch_national_flag(nums: list[int]):
        # 75. Sort Colors
        # 20min algs invented by Dijkstra
        i = j = 0
        k = len(nums) - 1
        pivot = 1

        # [:i] < pivot, [i:j] = pivot, [j:k+1] not yet sorted, [k+1:] > pivot
        while j <= k:
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > pivot:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1

    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return

        # do the left interval
        self.merge_sort(A, start, (start + end) // 2, temp)
        # do the right interval
        self.merge_sort(A, (start + end) // 2 + 1, end, temp)
        # merge sorted left/right intervals
        self.merge(A, start, end, temp)

    def merge(self, A, start, end, temp):
        middle = (start + end) // 2
        left_idx = start
        right_idx = middle + 1
        idx = start

        while left_idx <= middle and right_idx <= end:
            if A[left_idx] < A[right_idx]:
                temp[idx] = A[left_idx]
                left_idx += 1
                idx += 1
            else:
                temp[idx] = A[right_idx]
                right_idx += 1
                idx += 1

        while left_idx <= middle:
            temp[idx] = A[left_idx]
            left_idx += 1
            idx += 1

        while right_idx <= end:
            temp[idx] = A[right_idx]
            right_idx += 1
            idx += 1

        for i in range(start, end + 1):
            A[i] = temp[i]


test = Solution()
A = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
# test.quick_sort(A, 0, len(A)-1)
# test.quick_sort_lomuto(A, 0, len(A) - 1)
# print(A)
print(sorted(A))
print(test.qselect(A, 0, len(A) - 1, k=0))
print(A)
print(test.qselect(A, 0, len(A) - 1, k=5))


# B = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
# temp = [0] * len(B)
# test.merge_sort(B, 0, len(B)-1, temp)
# print(B)
