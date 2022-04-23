"""
https://leetcode.com/list?selectedList=5f4y8dwj
Must Do Easy Questions
"""

MP = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        def os_l2r():
            total = 0
            i = 0
            while i < len(s):
                # If this is the subtractive case.
                if i + 1 < len(s) and MP[s[i]] < MP[s[i + 1]]:
                    total += MP[s[i + 1]] - MP[s[i]]
                    i += 2
                # Else this is NOT the subtractive case.
                else:
                    total += MP[s[i]]
                    i += 1
            return total

        def os_r2l():
            """
            Runtime: 48 ms, faster than 74.99% of Python3 online submissions for Roman to Integer.

            REF: OS: Understanding the problem, find pattern (forward vs backward thinking)
            """
            ans = MP[s[-1]]
            for i in reversed(range(len(s)-1)):
                if MP[s[i]] < MP[s[i+1]]:
                    ans -= MP[s[i]]
                else:
                    ans += MP[s[i]]
            return ans

        def fxr():
            """
            Runtime: 52 ms, faster than 59.53% of Python3 online submissions for Roman to Integer.

            AC in 1.
            """
            # RO = 'IVXLCDM'
            # Edges = list(zip(RO, RO[1:]))
            EDGES = {
                'IV': 4,
                'IX': 9,
                'XL': 40,
                'XC': 90,
                'CD': 400,
                'CM': 900,
            }

            ans = 0
            i = 0
            while i < len(s):
                if i+1 < len(s):
                    ii1 = ''.join(s[i:i+2])
                    if ii1 in EDGES:
                        ans += EDGES[ii1]
                        i += 2
                        continue
                ans += MP[s[i]]
                i += 1
            return ans
        # return fxr()
        # return os_l2r()
        return os_r2l()


sl = Solution()
ss = ['III', 'IV', 'IX', 'XL', 'LVIII', 'MCMXCIV']  # ['IX', 'IM']  #

for s in ss:
    print(sl.romanToInt(s))
