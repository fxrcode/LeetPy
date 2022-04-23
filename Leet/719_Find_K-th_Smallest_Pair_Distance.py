'''
https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1041/
Leetcode Explore: Binary Search - More Practice II

The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

HINT: Binary search for the answer. How can you check how many pairs have distance <= X?

Ultimate post by fun4LeetCode: <Approach the problem using the "trial and error" algorithm>
https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/109082/Approach-the-problem-using-the-%22trial-and-error%22-algorithm



XXX: Reframe origin problem (alternative definition of key var: K-th smallest pair distance)
✅ GOOD Binary Search (k-th min/max/freq) in set
济公学院: https://www.youtube.com/watch?v=DD8RD7tx6V4
* Common pattern reframe problem into generic binary search f(v), by `count(pairs)>=k`.
    * Generic: Find the turning point in an ordered boolean function f(v).
    * Ordered: f(v) <= f(v+1) for any v where we take 0=false and 1=true.
    * Turning point: Find v' such that f(v')=false and f(v*' + 1)=true.
    * Example: f(0)=f(1)=...=f(3)=false, f(4)=f(5)=...=f(8)=true where v'=3 is the turning point.


Lastly here is a list of LeetCode problems that can be solved using the trial and error algorithm (you're welcome to add more examples):

786. K-th Smallest Prime Fraction
774. Minimize Max Distance to Gas Station
719. Find K-th Smallest Pair Distance
668. Kth Smallest Number in Multiplication Table
644. Maximum Average Subarray II
378. Kth Smallest Element in a Sorted Matrix
'''

from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def smallestDistancePair_jigong(self, nums: List[int], k: int) -> int:
        """
        Your runtime beats 51.91 % of python3 submissions.

        ✅ 济公学院: https://www.youtube.com/watch?v=DD8RD7tx6V4
        XXX: this is not hard if you really understand generic binary search and pattern
            * k-th xxx (max/min/freq) in set <=> Given constant val, search if exists subset that count(<=val) >= k.
        """
        nums.sort()

        def f(k, val) -> bool:
            # XXX: Common snippet
            # bool func: if there're k pairs whose distance <= val
            count = 0
            rloc = 0
            for i in range(len(nums)):
                while rloc < len(nums) and nums[rloc] - nums[i] <= val:
                    rloc += 1
                count += rloc - 1 - i
            return count >= k

        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            if f(k, mid):
                r = mid
            else:
                l = mid + 1
        return l

    def smallestDistancePair_heapq(self, nums: List[int], k: int) -> int:
        """
        TLE: 16 / 19 test cases passed.

        XXX: Official Solution I. I should have think about this: nums, kth-something: obvious heapq.
        But I was thinking only about binary search.
        <The Art and Craft of Problem Solving>: in beginning of problem, open your mind, try differnt routes like Polya's mouse!

        because the heapq.heapify operation is linear time.
        T: O(nlogn + N + k * logn ), max(k) = n*(n-1)/2 => T: O((n^2)logn).
        """
        nums.sort()
        n = len(nums)
        pq = [(nums[i + 1] - nums[i], i, i + 1) for i in range(n - 1)]
        heapify(pq)

        for _ in range(k):
            d, root, nei = heappop(pq)
            if nei + 1 < n:
                heappush(pq, (nums[nei + 1] - nums[root], root, nei + 1))
        return d

    @staticmethod
    def countPairDistLessEqualK(nums: List[int], k: int, val: int) -> bool:
        """
        XXX: Classic 2 pointers O(N) question: if count(d_ij <= val) >= k?
        If len(nums) = n, how many total pairs? Ans: (n-1)+(n-2)+ ... +1 = (1+n)*n/2

        XXX: why T: O(N)? ans: inner loop never return, so it's mono incr.
        """
        nums.sort()
        count, rloc = 0, 0
        for i in range(len(nums)):
            while rloc < len(nums) and nums[rloc] - nums[i] <= val:
                rloc += 1
            count += rloc - i - 1
        return count >= k


sl = Solution()
# print(Solution.countPairDistLessEqualK([5, 8], k=2, val=3))
print(sl.smallestDistancePair_heapq(nums=[1, 3, 1], k=2))
print(sl.smallestDistancePair_jigong(nums=[1, 3, 1], k=2))
