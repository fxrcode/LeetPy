from collections import deque
from typing import List


class ZigzagIterator(object):
    """
    https://leetcode.com/problems/zigzag-iterator/discuss/71786/Python-O(1)-space-solutions
    Runtime: 68 ms, faster than 22.37% of Python3 online submissions for Zigzag Iterator.

    """

    def __init__(self, v1, v2):
        self.data = [(len(v), iter(v)) for v in (v1, v2) if v]

    def next(self):
        len, iter = self.data.pop(0)
        if len > 1:
            self.data.append((len - 1, iter))
        return next(iter)

    def hasNext(self):
        return bool(self.data)


class ZigzagIterator_fxr:
    """
    Can't handle after last number
    """

    def __init__(self, v1: List[int], v2: List[int]):
        self.its = deque([iter(v1), iter(v2)])
        self.still = True

    def next(self) -> int:
        it = self.its.popleft()
        v = next(it, None)
        while not v:
            if not self.its:
                self.still = False
                raise Exception
            it = self.its.popleft()
            v = next(it, None)
        self.its.append(it)
        return v

    def hasNext(self) -> bool:
        return self.still


class ZigzagIterator_MeiqiGuo:
    """
    Runtime: 48 ms, faster than 86.96% of Python3 online submissions for Zigzag Iterator.

    REF: https://leetcode.com/problems/zigzag-iterator/discuss/229199/Python-simple-code-O(k)-space-beat-100
    XXX: smart usage of deque popleft then append to make it circular!
    BAD: but it uses count so failed in stream iterator
    """

    def __init__(self, v1: List[int], v2: List[int]):
        self.v = [deque(v1), deque(v2)]
        self.vec_idx = deque(range(len(self.v)))
        self.count = sum(len(x) for x in self.v)

    def next(self) -> int:
        idx = self.vec_idx.popleft()
        while not self.v[idx]:
            idx = self.vec_idx.popleft()
        v = self.v[idx].popleft()
        self.count -= 1
        self.vec_idx.append(idx)
        return v

    def hasNext(self) -> bool:
        return self.count > 0


zig = ZigzagIterator(v1=[1, 2], v2=[3, 4, 5, 6])
ans = []
while zig.hasNext():
    ans.append(zig.next())
print(ans)
