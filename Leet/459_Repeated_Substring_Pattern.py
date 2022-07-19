"""
Tag: Easy, FB
Lookback:

"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def rsrs3():
            """
            Runtime: 28 ms, faster than 95.71% of Python3 online submissions for Repeated Substring Pattern.

            T: O(N)

            Prove:
            * Consider a string S="helloworld". Now, given another string T="lloworldhe",
                can we figure out if T is a rotated version of S? Yes, we can! We check if S is a substring of T+T.
                detail prove: https://leetcode.com/problems/repeated-substring-pattern/discuss/826151/Python-by-fold-and-find-w-Simple-proof
            """
            return s in (2 * s)[1:-1]

        def DBabichev():
            """
            Runtime: 68 ms, faster than 63.65% of Python3 online submissions for Repeated Substring Pattern.

            T: O(N)
            """
            N = len(s)
            for l in range(1, N // 2 + 1):
                if N % l == 0 and s[:l] * (N // l) == s:
                    return True
            return False

        def fxr():
            """
            Runtime: 110 ms, faster than 44.11% of Python3 online submissions for Repeated Substring Pattern.

            T: O(L)
            """
            for l in range(1, len(s)):
                if len(s) % l != 0:
                    continue
                pref = s[:l]
                for i in range(len(s) // l):
                    if s[i * l : i * l + l] != pref:
                        break
                else:
                    # The else clause executes after the loop completes normally. This means that the loop did not encounter a break statement.
                    return True
            return False

        return fxr()


sl = Solution()
print(sl.repeatedSubstringPattern("abab"))
print(sl.repeatedSubstringPattern("aba"))
