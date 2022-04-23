'''
FB tag (medium)

Lookback:
+ think general case, then comes with algs.
+ only code with verified algs!
+ never patch code randomly for specific cases in interview!
'''


class Solution:
    def breakPalindrome(self, pal: str) -> str:
        def os():
            """
            Runtime: 40 ms, faster than 30.73% of Python3 online submissions for Break a Palindrome.

            XXX: DBabichev
            """
            for i in range(len(pal) // 2):
                if pal[i] != 'a':
                    return pal[:i] + 'a' + pal[i + 1:]
            return pal[:-1] + 'b' if pal[:-1] else ''

        return os()

        def fxr():
            """
            Runtime: 46 ms, faster than 20.88% of Python3 online submissions for Break a Palindrome.

            AC after 3 WA... Ugly
            """
            l = len(pal)
            ans = []
            if l == 1:
                return ''
            i = 0
            while i < l - 1:
                if pal[i] > 'a':
                    break
                i += 1
            if i == l // 2 and l % 2 == 1:
                ans = pal[:-1] + 'b'
                return ''.join(ans)
            c = 'a'
            if pal[i] == 'a':
                c = 'b'
            ans = pal[:i] + c + pal[i + 1:]
            return ''.join(ans)

        return fxr()


sl = Solution()
ss = ['abccba', 'aaa', 'aba', "aabaa"]
for s in ss:
    print(sl.breakPalindrome(s))