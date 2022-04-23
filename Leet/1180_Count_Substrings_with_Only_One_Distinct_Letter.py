'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''


from typing import List


class Solution:
    def countLetters(self, s: str) -> int:
        def hjt486():
            """
            Runtime: 46 ms, faster than 19.18% of Python3 online submissions for Count Substrings with Only One Distinct Letter.

            Do the 1+2+...+n on the fly.
            T: O(N)
            """
            S = ' ' + s + ' '
            total, count = 0, 1
            for i in range(1, len(S)-1):
                if S[i] != S[i-1]:
                    count = 1
                else:
                    count += 1
                total += count
            return total

        def fxr():
            """
            Runtime: 64 ms, faster than 8.49% of Python3 online submissions for Count Substrings with Only One Distinct Letter.

            AC in 1min.
            T: O(N)
            """
            def times(x): return x*(x+1)//2
            i = 0
            ans = 0
            while i < len(s):
                c = s[i]
                j = i
                while j < len(s) and s[j] == c:
                    j += 1
                same = j-i
                # print(c, same)
                ans += times(same)
                i = j
            return ans

        return fxr()


sl = Solution()
print(sl.countLetters('aaaba'))
print(sl.countLetters(s="aaaaaaaaaa"))
