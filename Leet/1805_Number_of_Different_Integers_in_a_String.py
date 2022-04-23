"""
tag: easy, string
Lookback:
- practice more on slide-window!
"""


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        def lee215():
            """
            Runtime: 36 ms, faster than 80.76% of Python3 online submissions for Number of Different Integers in a String.

            """
            s = "".join(c if c.isdigit() else " " for c in word)
            return len(set(map(int, s.split())))

        def fxr():
            """
            Runtime: 43 ms, faster than 63.58% of Python3 online submissions for Number of Different Integers in a String.

            """
            nums = set()
            l, r = 0, 0
            while l < len(word):
                if word[l].isalpha():
                    l += 1
                else:
                    r = l
                    while r < len(word) and word[r].isdigit():
                        r += 1
                    nums.add(int(word[l:r]))
                    l = r
            return len(nums)

        return fxr()


sl = Solution()
for w in ["a123bc34d8ef34", "leet1234code234", "a1b01c001"]:
    print(sl.numDifferentIntegers(w))
