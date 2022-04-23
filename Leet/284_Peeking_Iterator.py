'''
Google, TuSimple prerequisite
https://leetcode.com/discuss/interview-question/345744/Google-or-Onsite-or-Merge-K-Sorted-Iterators
'''
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    """
    Runtime: 38 ms, faster than 16.61% of Python3 online submissions for Peeking Iterator.

    os Approach 2: Saving the Next Value
    """

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nx = iterator.next()
        self.it = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nx

    def next(self):
        """
        :rtype: int
        """
        if self.nx is None:
            raise StopIteration()
        ret = self.nx
        self.nx = None
        if self.it.hasNext():
            self.nx = self.it.next()
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nx is not None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
