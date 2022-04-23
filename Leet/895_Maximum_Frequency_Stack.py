"""
Daily Challenge (Mar 19, 2022)
tag: Hard, Hash
Lookback:
- How to analyze problem? 
- What DSA to choose?
- Be creative
"""

from collections import Counter, defaultdict


class FreqStack:
    """
    Runtime: 335 ms, faster than 76.57% of Python3 online submissions for Maximum Frequency Stack.

    OS/Neet: no need to del empty gruops
    """

    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)
        self.mxfreq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.mxfreq:
            self.mxfreq = f
        self.group[f].append(val)

    def pop(self) -> int:
        x = self.group[self.mxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.mxfreq]:
            self.mxfreq -= 1
        return x


class FreqStack_fxr:
    """
    Your runtime beats 52.20 % of python3 submissions.

    """

    def __init__(self):
        self.cnt_group = defaultdict(list)
        self.mx_cnt = 0
        self.v2cnt = defaultdict(int)

    def push(self, val: int) -> None:
        self.v2cnt[val] += 1
        f = self.v2cnt[val]
        self.cnt_group[f].append(val)
        self.mx_cnt = max(self.mx_cnt, f)

    def pop(self) -> int:
        f = self.mx_cnt
        v = self.cnt_group[f].pop()
        if not self.cnt_group[f]:
            del self.cnt_group[f]
            self.mx_cnt -= 1
        self.v2cnt[v] -= 1
        if self.v2cnt[v] == 0:
            del self.v2cnt[v]
        return v


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
