"""
✅ GOOD min/max heap to get k-th min/max.

https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75

? Followup: If all (or 99%) integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
1093. Statistics from a Large Sample
"""
from heapq import heappop, heappush

from sortedcontainers import SortedList


class MedianFinder_BST:
    """
    https://leetcode.com/problems/find-median-from-data-stream/discuss/1330646/C%2B%2BJavaPython-MinHeap-MaxHeap-Solution-Picture-explain-Clean-and-Concise
    XXX: use red-black tree to sort keys (overkill), and slower
        findMedian: O(logN) while heap's impl is O(1)!
    """

    def __init__(self) -> None:
        self.arr = SortedList()

    def addNum(self, n):
        self.arr.add(n)

    def findMedian(self):
        n = len(self.arr)
        if n % 2 == 1:
            return self.arr[n // 2]
        return (self.arr[n // 2] + self.arr[n // 2 - 1]) / 2


class MedianFinder:
    """
    Runtime: 588 ms, faster than 83.49% of Python3 online submissions for Find Median from Data Stream.

    https://leetcode.com/problems/find-median-from-data-stream/solution/
    """

    def __init__(self) -> None:
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        """
        OS re-balancing
        XXX: how to think? invariant: lo >= hi, so when odd, the median = lo[0]
            init: lo = [], hi=[]
            add(5): lo=[5], hi=[]
            add(10): lo=[5], hi=[10]
            add(6): lo=[5,6], hi=[10]
            add(11): lo=[5,6], hi=[11]

        """
        heappush(self.lo, -num)
        heappush(self.hi, -heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heappush(self.lo, -heappop(self.hi))

    def findMedian(self):
        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0]) / 2
        else:
            return -self.lo[0]

    """
    def addNum_pepsi(self, num: int) -> None:
        # XXX: dietpepsi re-balancing
        if len(self.lo) == len(self.hi):
            heappush(self.lo, -heappushpop(self.hi, num))
        else:
            heappush(self.hi, -heappushpop(self.lo, -num))
    """


class MedianFinder_fxr:
    """
    Runtime: 516 ms, faster than 93.66% of Python3 online submissions for Find Median from Data Stream.

    Spent 30min to debug!
    XXX: should code after have clear algs!!!
    """

    def __init__(self):
        self.mxh = []  # lower half
        self.mnh = []  # upper half

    def addNum(self, num: int) -> None:
        if not self.mxh:
            self.mxh.append(-num)
            return

        if len(self.mxh) == len(self.mnh):
            if num <= self.mnh[0]:
                heappush(self.mxh, -num)
            else:
                tmp = heappop(self.mnh)
                heappush(self.mxh, -tmp)
                heappush(self.mnh, num)
        else:  # left > right
            if num <= -self.mxh[0]:
                tmp = -heappop(self.mxh)
                heappush(self.mnh, tmp)
                heappush(self.mxh, -num)
            else:
                heappush(self.mnh, num)

    def findMedian(self) -> float:
        len_mx = len(self.mxh)
        len_mn = len(self.mnh)
        if len_mx > len_mn:
            ans = -self.mxh[0]
            print(ans, "\t", self.mxh, self.mnh)
            return ans
        else:
            lowermid = -self.mxh[0]
            uppwermid = self.mnh[0]
            med = (lowermid + uppwermid) / 2
            print(med, "\t", self.mxh, self.mnh)
            return med


"""
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
"""
finder = MedianFinder()
# finder.addNum(-1)
# finder.findMedian()
# finder.addNum(-2)
# finder.findMedian()
# finder.addNum(-3)
# finder.findMedian()
# finder.addNum(-4)
# finder.findMedian()

finder.addNum(6)
finder.findMedian()
finder.addNum(10)
finder.findMedian()
finder.addNum(2)
finder.findMedian()
finder.addNum(6)
finder.findMedian()
finder.addNum(5)
finder.findMedian()
finder.addNum(0)
finder.findMedian()
finder.addNum(6)
finder.findMedian()
finder.addNum(3)
finder.findMedian()
finder.addNum(1)
finder.findMedian()
finder.addNum(0)
finder.findMedian()
finder.addNum(0)
finder.findMedian()


# finder.addNum(40)
# finder.findMedian()
# finder.addNum(12)
# finder.findMedian()
# finder.addNum(16)
# finder.findMedian()
