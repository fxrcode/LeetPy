'''
https://leetcode.libaoj.in/minimum-swaps-to-group-all-1s-together.html
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

Example 1:
Input: data = [1,0,1,0,1]
Output: 1
Explanation:
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.

Hints:
1. How many 1's should be grouped together ? Is not a fixed number?
2. Yeah it's just the number of 1's the whole array has. Let's name this number as ones
3. Every subarray of size of ones, needs some number of swaps to reach, Can you find the number of swaps needed to group all 1's in this subarray?
4. It's the number of zeros in that subarray.
5. Do you need to count the number of zeros all over again for every position ?
6. Use Sliding Window technique.

TODO: Followup: Minimum swaps required to bring all elements less than or equal to k together
https://www.geeksforgeeks.org/minimum-swaps-required-bring-elements-less-equal-k-together/
'''


from typing import List
from collections import deque


class Solution:
    def minSwaps_2ptr(self, data: List[int]) -> int:
        """
        Runtime: 1336 ms, faster than 5.06% of Python3 online submissions for Minimum Swaps to Group All 1's Together.
        T: O(n)
        XXX: the window of 1's is fixed. Just need to slide the window to find the window with max 1's
        Approach 1: Sliding window using 2 pointers
        and daleitai (staging) to update global max_ones with all window's cnt_one
        """
        ones = data.count(1)
        n = len(data)
        l, r = 0, 0
        cnt_one, max_one = 0, 0
        while r < n:
            c = data[r]
            r += 1
            cnt_one += c
            print(l, r, cnt_one, max_one)
            while r-l > ones:
                d = data[l]
                l += 1
                cnt_one -= d
            # now r-l = ones
            max_one = max(max_one, cnt_one)
        return ones - max_one

    def minSwaps_deque(self, data: List[int]) -> int:
        """
        Approach 2: Sliding window with Deque
        T: O(n). M: O(n) for the deque
        """
        ones = sum(data)
        cnt_one = max_one = 0
        q = deque()
        for i in range(len(data)):
            c = data[i]
            q.append(c)
            cnt_one += c
            while len(q) > ones:
                d = q.popleft()
                cnt_one -= d
            max_one = max(max_one, cnt_one)
        return ones - max_one


sl = Solution()

data = [1, 0, 1, 0, 1]
print(sl.minSwaps(data))
