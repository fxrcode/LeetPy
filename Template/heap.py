from heapq import heappop, heappush


class Example:
    @staticmethod
    def first_k_smallest(A, k):
        pq = []
        for i, a in enumerate(A):
            heappush(pq, (-a, i))
            if len(pq) > k:
                heappop(pq)
        print([A[i] for _, i in pq])

    @staticmethod
    def biggest_k(A, k):
        pq = []
        for i, a in enumerate(A):
            heappush(pq, (a, i))
            if len(pq) > k:
                heappop(pq)
        print([A[i] for _, i in pq])


ex = Example()
ex.first_k_smallest([3, 1, 5, 4, 2], 2)
ex.biggest_k([3, 1, 5, 4, 2], 2)


class Heap:

    """
    XXX: from 9chap template
    heap + function to delete specific node with lazy-deletion
    Use case
    ---
    * find max/min value
    * find kth minimum, O(nlogK)
    * if required O(logN) operation
    """

    def __init__(self) -> None:
        self.minheap = []
        self.deleted_set = set()

    def push(self, index, val):
        heappush(self.minheap, (val, index))

    def _lazy_deletion(self):
        """internal method to improve default heap as binary heap"""
        while self.minheap and self.minheap[0][1] in self.deleted_set:
            heappop(self.minheap)

    def top(self):
        self._lazy_deletion()
        return self.minheap[0]

    def pop(self):
        self._lazy_deletion()
        heappop(self.minheap)

    def delete(self, index):
        self.deleted_set.add(index)

    def is_empty(self):
        return not bool(self.minheap)
