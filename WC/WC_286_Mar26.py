"""
Weekly contest 286 (Mar 26, 2022) 7:30pm-9:00pm
2/4
Very weak in logic and coding skills (Q2,Q3)
"""

from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def kth_len(k, l):
            # l, has l//2
            total = 10 ** ((l - 1) // 2) * 9
            if k > total:
                return -1
            k -= 1
            ans = [0] * l
            start = 10 ** ((l - 1) // 2)
            out = True
            i = 0
            while i < (l + 1) // 2:
                v, k = divmod(k, start)
                ans[i] = ans[~i] = v + 1 if out else v
                i += 1
                out = False
                start //= 10
            # return "".join(map(str, ans))
            x = 0
            for n in ans:
                x = 10 * x + n
            return x

        res = []
        for q in queries:
            res.append(kth_len(q, intLength))
        return res

        print(kth_len(10, 1))

    def minDeletion(self, nums: List[int]) -> int:
        j = 0
        last = None
        res = []
        i = 0
        while i < len(nums):
            if j % 2 == 0:
                res.append(i)
                last = nums[i]
            else:
                while i < len(nums) and nums[i] == last:
                    i += 1
                # nums[i] != last
                if i == len(nums):
                    break
                # print(i)
                last = nums[i]
                res.append(i)
            i += 1
            j += 1
        if len(res) % 2 != 0:
            res.pop()
        return len(nums) - len(res)


sl = Solution()
# print(sl.minDeletion(nums=[1, 1, 2, 3, 5]))
# print(sl.minDeletion(nums=[1, 1, 2, 2, 3, 3]))

print(sl.kthPalindrome(queries=[1, 2, 3, 4, 5, 90], intLength=3))
print(sl.kthPalindrome(queries=[2, 4, 6], intLength=4))


def kth_len(k, l):
    # l, has l//2
    total = 10 ** (l // 2) * 9
    if k > total:
        return -1
    k -= 1
    ans = [0] * l
    start = 10 ** (l // 2)
    out = True
    i = 0
    while i < (l + 1) // 2:
        v, k = divmod(k, start)
        ans[i] = ans[~i] = v + 1 if out else v
        i += 1
        out = False
        start //= 10
    # return "".join(map(str, ans))
    x = 0
    for n in ans:
        x = 10 * x + n
    return x


print(kth_len(90, 3))
