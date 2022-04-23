'''
✅ GOOD Top k elements

Explore Array & String
https://leetcode.com/problems/maximum-product-of-three-numbers/
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

* similar: 414. Third Maximum Number

'''


from typing import List


class Solution:
    # def maximumProduct(self, nums: List[int]) -> int:

    def maximumProduct_sort(self, nums: List[int]) -> int:
        """
        O(nlogn)
        Runtime: 260 ms
        """
        nums.sort()
        n = len(nums)
        c1 = nums[0]*nums[1]*nums[n-1]
        c2 = nums[-1] * nums[-2] * nums[-3]
        return max(c1, c2)

    def maximumProduct(self, nums: List[int]) -> int:
        """
        WA: [0,0,0] => nan, rather 0.
        Runtime: 276 ms, faster than 35.98% of Python3 online submissions for Maximum Product of Three Numbers.
        """
        vmx = [float('-inf')]*3
        vmn = [float('inf')]*2
        for n in nums:
            # to update v max
            if n > vmx[0]:
                vmx = [n, vmx[0], vmx[1]]
            elif n > vmx[1]:
                vmx = [vmx[0], n, vmx[1]]
            elif n > vmx[2]:
                vmx = [vmx[0], vmx[1], n]
            # to update v min
            if n < vmn[0]:
                vmn = [n, vmn[0]]
            elif n < vmn[1]:
                vmn = [vmn[0], n]

        print(vmx, vmn)

        return max(vmx[0]*vmx[1]*vmx[2], vmn[0]*vmn[1]*vmx[0])

    '''
    def maximumProduct_BUG(self, nums: List[int]) -> int:
        def shift(n: int, v: List[int]) -> None:
            if n in v:
                return
            if n > v[0]:
                v = v[n, v[0], v[1]]
            elif n > v[1]:
                v = v[v[0], n, v[1]]
            elif n > v[2]:
                v = v[v[0], v[1], n]

        # 1st max, 2nd max, 3rd max
        vp = [float('-inf'), float('-inf'), float('-inf')]
        # 1st min, 2nd min, 3rd min
        vn = [float('-inf'), float('-inf'), float('-inf')]

        for i, n in enumerate(nums):
            if n >= 0:
                shift(n, vp)
            else:
                shift(-n, vn)
    '''


nums = [-3, -2, 0, 9]
sl = Solution()
print(sl.maximumProduct(nums))
print(sl.maximumProduct([0, 0, 0]))
