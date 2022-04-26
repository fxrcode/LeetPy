"""
✅ GOOD Design (DSA)
tag: Medium, Design
Lookback:
- Greedy vs Lazy

Google, TuSimple prerequisite
https://leetcode.com/discuss/interview-question/345744/Google-or-Onsite-or-Merge-K-Sorted-Iterators
"""
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


class PeekingIterator_Greedy:
    """
    Runtime: 62 ms, faster than 12.25% of Python3 online submissions for Peeking Iterator.
    https://leetcode.com/problems/peeking-iterator/discuss/1055977/Python-3-Greedy-and-lazy-24ms
    """

    def __init__(self, iterator):
        self._iterator = iterator
        self._current = None
        self._hasNext = True
        self.next()

    def peek(self):
        return self._current

    def next(self):
        current = self._current
        if self._iterator.hasNext():
            self._current = self._iterator.next()
        else:
            self._hasNext = False

        return current

    def hasNext(self):
        return self._hasNext


class PeekingIterator_Lazy:
    """
    Runtime: 68 ms, faster than 5.42% of Python3 online submissions for Peeking Iterator.
    https://leetcode.com/problems/peeking-iterator/discuss/1055977/Python-3-Greedy-and-lazy-24ms
    """

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iter = iterator
        self._peeked = False
        self._cur = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self._peeked:
            self._cur = self._iter.next()
            self._peeked = True
        return self._cur

    def next(self):
        """
        :rtype: int
        """
        if self._peeked:
            self._peeked = False
        else:
            self._cur = self._iter.next()
        return self._cur

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._peeked or self._iter.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
