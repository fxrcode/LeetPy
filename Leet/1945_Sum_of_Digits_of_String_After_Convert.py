'''
tag: easy

similar: 258.Add Digits
'''


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def fxr():
            """
            Runtime: 62 ms, faster than 19.97% of Python3 online submissions for Sum of Digits of String After Convert.

            """
            def sumdig(v):
                return sum(map(int, str(v)))

            k0 = int(''.join([str(ord(c) - ord('`')) for c in s]))
            for _ in range(k):
                k0 = sumdig(k0)
            return k0

        return fxr()


sl = Solution()
# s = 'zbax'
# s = "iiii"
s = "leetcode"
k = 2
print(sl.getLucky(s, k))