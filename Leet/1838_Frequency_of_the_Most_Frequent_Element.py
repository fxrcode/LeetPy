"""
✅ GOOD 2ptr (Slide-window)
tag: Medium, 2ptr, Slide-window
Lookback:
- classic Slide-window
- C++ Maximum Sliding Window Cheatsheet Template!
[ ] REDO

Problems Solvable using this template
3. Longest Substring Without Repeating Characters
159. Longest Substring with At Most Two Distinct Characters (Medium)
340. Longest Substring with At Most K Distinct Characters
424. Longest Repeating Character Replacement
487. Max Consecutive Ones II
713. Subarray Product Less Than K
1004. Max Consecutive Ones III
1208. Get Equal Substrings Within Budget (Medium)
1493. Longest Subarray of 1's After Deleting One Element
1695. Maximum Erasure Value
1838. Frequency of the Most Frequent Element
2009. Minimum Number of Operations to Make Array Continuous
2024. Maximize the Confusion of an Exam
The following problems are also solvable using the shrinkable template with the "At Most to Equal" trick

930. Binary Subarrays With Sum (Medium)
992. Subarrays with K Different Integers
1248. Count Number of Nice Subarrays (Medium)
2062. Count Vowel Substrings of a String (Easy)
"""

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        def lzl124631x_Sasuke():
            """
            Runtime: 1496 ms, faster than 89.70% of Python3 online submissions for Frequency of the Most Frequent Element.

            https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/1175088/C%2B%2B-Maximum-Sliding-Window-Cheatsheet-Template!
            """
            nums.sort()
            ans = 1
            l, win_sm = 0, 0
            for r in range(len(nums)):
                # Greedy property: no need to clear win_sm but reuse, reminds me #828. Guo
                # Why? because sorted, larger target, means more left number cost more ops, so NOT possible in window!
                win_sm += nums[r]
                while (r - l + 1) * nums[r] - win_sm > k:
                    win_sm -= nums[l]
                    l += 1
                ans = max(ans, r - l + 1)
            return ans

        return lzl124631x_Sasuke()


sl = Solution()
print(sl.maxFrequency(nums=[1, 2, 4], k=5))
print(sl.maxFrequency(nums=[1, 4, 8, 13], k=5))
print(sl.maxFrequency(nums=[3, 9, 6], k=2))
