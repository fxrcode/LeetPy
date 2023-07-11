class Solution:
    def rotatedDigits(self, n: int) -> int:
        def incog():
            remains, skips, count = "2569", "347", 0

            for val in range(1, n + 1):
                val = str(val)
                if any(skip in val for skip in skips):
                    continue
                if any(remain in val for remain in remains):
                    count += 1
            return count

        return incog()

        def fxr():
            """
            Runtime: 192 ms, faster than 12.59% of Python3 online submissions for Rotated Digits.

            T: O(n*l) # l=digits(v)
            """
            d = {0: 0, 1: 1, 2: 5, 5: 2, 6: 9, 8: 8, 9: 6}

            def rev(v):
                vv = str(v)

                ans = 0
                for c in vv:
                    if int(c) not in d:
                        return -1
                    ans = ans * 10 + d[int(c)]
                return ans

            ans = []
            for i in range(1, n + 1):
                ri = rev(i)
                # print(i, ri)
                if ri not in (-1, i):
                    ans.append(i)
            print(ans)
            return len(ans)

        return fxr()


sl = Solution()
print(sl.rotatedDigits(n=20))
