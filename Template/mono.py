"""
# Mono-Stack vs Mono-Queue vs Sliding Window

古城算法: 基础算法 (六) --单调栈
https://www.bilibili.com/video/BV17z4y1y7tS
PPT: https://docs.google.com/presentation/d/1r4uWF4SkO8jQlZkqnJ57ZWP2p-T-OOZh8_jMCotYsPI/edit#slide=id.p

496. Next Greater Element I
503. Next Greater Element II
1019. Next Greater Node In Linked List
739. Daily Temperatures
316. Remove Duplicate Letters
1081. Smallest Subsequence of Distinct Characters
402. Remove K Digits
42. Trapping Rain Water
84. Largest Rectangle in Histogram

---

To Solve 84. Largest Rectangle in Histogram, I need better understanding of mono-stack
https://www.geeksforgeeks.org/next-greater-element/
https://www.geeksforgeeks.org/next-smaller-element/
https://www.geeksforgeeks.org/previous-greater-element/
https://www.geeksforgeeks.org/find-the-nearest-smaller-numbers-on-left-side-in-an-array/

* Next Greater/Smaller element (NGE, NSE)
* Previous Greater/Smaller element (PGE, PSE)

Q: Why Stack, mono-increase vs descrease? loop normal or reverse?
"""


from typing import List

# TODO: focus on 古城模板

'''
# DEPRECATED
def nextGreaterElements(nums: List[int]) -> List[int]:
    def method1():
        # simple O(N^2)
        res = []
        for i in range(len(nums)):
            nge = -1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    nge = nums[j]
                    break
            res.append(nge)

        print(res)

    def method2():
        # optimize with stack: O(N)
        stk = []
        for i in range(len(nums)):
            next = nums[i]
            while stk and stk[-1] < next:
                print(f"{stk.pop()} --> {next}")
                # ans.append(next)
            stk.append(next)
        # but the order may not be the same as input array
        while stk:
            print(f"{stk.pop()}--> -1")

    def method3():
        # optimize with stack: O(N), and also same order as input array
        stk = []
        ans = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            while stk and stk[-1] <= nums[i]:
                stk.pop()
            ans[i] = -1 if not stk else stk[-1]
            stk.append(nums[i])
        print(ans)

    """
    method1()
    method2()
    """
    method3()

def nextSmallerElements(nums: List[int]) -> List[int]:
    def method1():
        ans = []
        for i in range(len(nums)):
            nse = -1
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nse = nums[j]
                    break
            ans.append(nse)
        print(ans)

    def method2():
        """
        This problem is similar to next greater element. Here we maintain items in increasing
        order in the stack (instead of decreasing in next greater element problem).

        """
        ans = [0] * len(nums)
        stk = []
        for i in range(len(nums) - 1, -1, -1):
            while stk and stk[-1] >= nums[i]:
                stk.pop()
            ans[i] = -1 if not stk else stk[-1]
            stk.append(nums[i])
        print(ans)

    """
    method1()
    """
    method2()


# nextGreaterElements(nums=[11, 13, 21, 3])
nextGreaterElements([2, 1, 2, 4, 3])
# nextSmallerElements(nums=[4, 8, 5, 2, 25, ])
'''
