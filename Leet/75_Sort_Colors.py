"""
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

Lookback:
- finally understood 3-way partition
- similar to lomuto partition
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Dutch national Flag: Dijkstra invented in 20min in cafe in 1956!
        "What is the shortest way to travel from Rotterdam to Groningen, in general: from given city to given city. It is the algorithm for the shortest path, which I designed in about twenty minutes. One morning I was shopping in Amsterdam with my young fiancée, and tired, we sat down on the café terrace to drink a cup of coffee and I was just thinking about whether I could do this, and I then designed the algorithm for the shortest path. As I said, it was a twenty-minute invention. In fact, it was published in '59, three years later. The publication is still readable, it is, in fact, quite nice. One of the reasons that it is so nice was that I designed it without pencil and paper. I learned later that one of the advantages of designing without pencil and paper is that you are almost forced to avoid all avoidable complexities. Eventually, that algorithm became to my great amazement, one of the cornerstones of my fame."
        """
        def os():
            # for all idx < p0 : nums[idx < p0] = 0
            # curr is an index of element under consideration
            p0 = curr = 0
            # for all idx > p2 : nums[idx > p2] = 2
            p2 = len(nums) - 1

            while curr <= p2:
                if nums[curr] == 0:
                    nums[p0], nums[curr] = nums[curr], nums[p0]
                    p0 += 1
                    curr += 1
                elif nums[curr] == 2:
                    nums[curr], nums[p2] = nums[p2], nums[curr]
                    p2 -= 1
                else:
                    curr += 1

        return os()


sl = Solution()
# nums = [2, 0, 1]
nums = [2, 0, 2, 1, 1, 0]
sl.sortColors(nums)
print(nums)
