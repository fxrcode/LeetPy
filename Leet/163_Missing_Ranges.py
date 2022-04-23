"""
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

"""


from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def os():
            """
            Runtime: 28 ms, faster than 85.24% of Python3 online submissions for Missing Ranges.

            XXX: OS video solution is so elegant: how to analyse problem, how to make algs generic (reduce edge cases)
            """

            def form_range(lo, hi):
                if lo == hi:
                    return str(lo)
                else:
                    return "->".join([str(lo), str(hi)])

            res = []
            prev = lower - 1
            for i in range(len(nums) + 1):
                cur = nums[i] if i < len(nums) else upper + 1
                if prev + 1 <= cur - 1:
                    res.append(form_range(prev + 1, cur - 1))
                prev = cur
            return res

        def fxr():
            """
            Runtime: 28 ms, faster than 85.58% of Python3 online submissions for Missing Ranges.

            metacognition: simple traverse num and compare with [lower,higher], edge: for missing single num: [num]
            AC in 2 after debug.
            """
            # if not nums:
            #     if lower == upper:
            #         return [str(lower)]
            #     else:
            #         return ['->'.join([str(lower), str(upper)])]
            ret = []
            i = lower
            j = 0
            while j < len(nums) and i < upper + 1:
                if nums[j] == i:
                    i += 1
                    j += 1
                elif nums[j] > i:
                    if nums[j] - 1 == i:
                        # ret += [i]
                        ret.append(str(i))
                    else:
                        # ret += [i, nums[j]-1]
                        ret.append("->".join([str(i), str(nums[j] - 1)]))
                    i = nums[j] + 1
                    j += 1
                else:
                    print(i, j)
            if i <= upper:
                # ret += [i, upper]
                if i == upper:
                    ret.append(str(i))
                else:
                    ret.append("->".join([str(i), str(upper)]))
            return ret

        # return fxr()
        return os()


sl = Solution()
print(sl.findMissingRanges(nums=[0, 1, 3, 50, 75], lower=0, upper=99))
print(sl.findMissingRanges(nums=[-1], lower=-2, upper=-1))
print(sl.findMissingRanges(nums=[-1], lower=-1, upper=-1))
print(sl.findMissingRanges(nums=[], lower=-3, upper=-1))
print(sl.findMissingRanges(nums=[-3], lower=-3, upper=-2))
