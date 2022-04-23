"""
WC 288 - Apr 9, 2022
Bad: 2/4

"""


from itertools import cycle
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        nums.sort()

        fn = lambda to: sum(max(0, to - xx) for xx in nums[::-1])  # balls sold

        # bisect_left (first True)
        lo, hi = nums[0], nums[-1] + k
        while lo < hi:
            mid = (lo + hi) // 2
            if fn(mid) >= k:  # FFFFTTT
                hi = mid
            else:
                lo = mid + 1

        to = lo
        print(to)
        for i in range(len(nums) - 1, -1, -1):
            diff = max(0, min(k, to) - nums[i])
            nums[i] += diff
            k -= diff
        print(nums)

        ans = nums[0]
        for n in nums[1:]:
            ans *= n
        return ans

    def minimizeResult(self, expression: str) -> str:
        left, right = expression.split("+")

        def toN(s):
            if not s:
                return 0
            else:
                return int(s)

        lp, rp = -1, -1
        ans = eval(expression)
        for l in range(len(left)):
            for r in range(len(right)):
                a, b = max(1, toN(left[:l])), toN(left[l:])
                c, d = toN(right[: r + 1]), max(1, toN(right[r + 1 :]))
                # ans = min(ans, a * (b + c) * d)
                if a * (b + c) * d < ans:
                    ans = a * (b + c) * d
                    lp, rp = l, r + 1
        if lp == rp == -1:
            return "(" + expression + ")"
        left, right = list(left), list(right)
        left[lp:lp] = "("
        right[rp:rp] = ")"
        return "".join(left + ["+"] + right)

    def largestInteger(self, num: int) -> int:
        odd, even = [], []
        for i, n in enumerate(str(num)):
            if int(n) % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        odd.sort()
        even.sort()
        res = []
        print(odd)
        for i in range(len(str(num))):
            res.append(odd.pop() if int(str(num)[i]) % 2 == 1 else even.pop())
        return int("".join(res))


sl = Solution()
# print(sl.largestInteger(1234))
# print(sl.largestInteger(65875))
# print(sl.minimizeResult("12+34"))
# print(sl.minimizeResult("999+999"))
# print(sl.minimizeResult(expression="247+38"))
# print(sl.maximumProduct(nums=[0, 4], k=7))
print(sl.maximumProduct(nums=[6, 3, 3, 2], k=2))
# print(sl.maximumProduct(nums=[3, 3, 3, 3], k=2))
