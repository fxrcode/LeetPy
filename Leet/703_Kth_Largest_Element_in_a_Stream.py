"""
tag: Easy, Heapq
Lookback:
- kth largest: minheap of size(k)
- kth smallest: maxheap of size(k)
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1018/
Leetcode Explore Binary Search Tree: Conclusion

"""
from heapq import heapify, heappop, heappush
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        Runtime: 167 ms, faster than 34.86% of Python3 online submissions for Kth Largest Element in a Stream.

        T: O(k + M*logk + N*logk) = O(Mlogk + Nlogk)
        M: O(k)
        """
        self.k = k
        self.heap = nums
        heapify(self.heap)
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        """[summary]
        XXX: Always be vigilant to access list by index for out of index!
        BUG: heappushpop(self.minpq, val)

        loop invariant: minheap[0] always the k-th largest element in stream.
        """
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]


"""
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
"""

kl = KthLargest(1, [-9])
kl.add(-3)
kl.add(-2)
kl.add(-4)
