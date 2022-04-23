'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''


from typing import List
from string import ascii_letters, digits


class StringIterator:
    """
    OS: on-demand (aka. Lazy) computation
    Runtime: 48 ms, faster than 72.37% of Python3 online submissions for Design Compressed String Iterator.

    """

    def __init__(self, compressedString: str):
        self.ptr = 0
        self.num = 0
        self.ch = ' '
        self.res = compressedString

    def dbg(self):
        print(self.ptr, self.num, self.ch)

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.num == 0:
            self.ch = self.res[self.ptr]
            self.ptr += 1
            while self.ptr < len(self.res) and self.res[self.ptr].isdigit():
                self.num = self.num * 10 + int(self.res[self.ptr])
                self.ptr += 1
        self.num -= 1
        self.dbg()
        return self.ch

    def hasNext(self) -> bool:
        return self.ptr != len(self.res) or self.num != 0


class StringIterator_fxr:
    """
    Runtime: 40 ms, faster than 95.09% of Python3 online submissions for Design Compressed String Iterator.

    AC after 30min debug
    FIXME: !TOOOOOO complicated
    """
    @staticmethod
    def f_get_digits(s, ori):
        v = 0
        i = ori
        while i < len(s):
            # if s[i] not in digits:
            #     v = int(s[ori:i])
            #     break
            if s[i] in digits:
                i += 1
            else:
                break
        return int(s[ori:i])

    def __init__(self, compressedString: str):
        self.chars = []
        self.ci = 0
        self.cs = compressedString
        for i, c in enumerate(compressedString):
            if c in ascii_letters:
                self.chars.append((i, c))
        v = self.f_get_digits(compressedString, 1)
        self.left = v

    def next(self) -> str:
        if not self.hasNext():
            print('nah')
            return ''
        _, c = self.chars[self.ci]
        self.left -= 1
        if self.left == 0:
            self.ci += 1
            if self.hasNext():
                # self.ci += 1
                i, _ = self.chars[self.ci]
                v = self.f_get_digits(self.cs, i+1)
                self.left = v
                # print(self.ci, self.left)
        print(c)
        return c

    def hasNext(self) -> bool:
        if self.ci == len(self.chars):
            return False
        return True


'''
# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
'''
# si = StringIterator("L1e2t1C1o1d1e1")
# si.next()
# si.next()
# si.next()
# si.next()
# si.next()
# si.next()
# si.hasNext()
# si.next()
# si.hasNext()

si = StringIterator("x2")
si.next()
si.next()
si.next()
si.next()
si.next()
si.next()
si.hasNext()
si.next()
si.hasNext()
si.next()
si.next()
si.next()
si.next()
