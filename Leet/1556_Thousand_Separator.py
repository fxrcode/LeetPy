class Solution:
    def thousandSeparator(self, n: int) -> str:
        def srushti22():
            # Your runtime beats 31.17 % of python3 submissions.
            s = str(n)
            s = s[::-1]
            res = '.'.join(s[i:i + 3] for i in range(0, len(s), 3))
            return res[::-1]

        return srushti22()

        def fxr():
            """
            Runtime: 37 ms, faster than 40.15% of Python3 online submissions for Thousand Separator.
            """
            s = str(n)
            if len(s) < 4:
                return s

            s = s[::-1]
            ret = [None] * len(s)
            for i in range(len(s)):
                ret[i] = s[i]
                if (i + 1) % 3 == 0:
                    ret[i] += '.'
            ans = ''.join(ret)[::-1]
            if ans[0] == '.':
                return ans[1:]
            return ans


sl = Solution()
for n in [987, 1234, 123456789]:
    print(sl.thousandSeparator(n))