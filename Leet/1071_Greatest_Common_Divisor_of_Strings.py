"""
✅ String (Logic)
date: 01312023
Tag: Easy, Logic, str
Lookback:
- 1st time GCD of str
- The proof of answer must be GCD(str1, str2)
- s1+s2 == s2+s1, due to (m+n)X === (n+m)X
    * reminds me 160. Intersection of 2 linked-list
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def os_cn():
            """
            Runtime: 28 ms, faster than 97.40% of Python3 online submissions for Greatest Common Divisor of Strings.

            https://leetcode-cn.com/problems/greatest-common-divisor-of-strings/solution/zi-fu-chuan-de-zui-da-gong-yin-zi-by-leetcode-solu/
            XXX: the length of gcd substring must be the gcd of the lengthes of both string.
            """

            def gcd(a, b):
                while b:
                    a, b = b, a % b
                return a

            d = gcd(len(str1), len(str2))
            if str1 + str2 == str2 + str1:
                return str1[:d]
            return ""

        return os_cn()


sl = Solution()
print(sl.gcdOfStrings(str1="ABCABC", str2="ABC"))
print(sl.gcdOfStrings(str1="ABABAB", str2="ABAB"))
print(
    sl.gcdOfStrings(
        "TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    )
)
print(sl.gcdOfStrings("AAAAAAAAA", "AAACCC"))
