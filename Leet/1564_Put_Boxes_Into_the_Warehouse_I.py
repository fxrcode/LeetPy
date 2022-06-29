"""
✅ GOOD Greedy (can't figure out question definition!)
Tag: Medium, Greedy, Sort
Lookback:
- multiple solutions based on perspective.
- think through via analogy
- Great OS: Let's think through an analogy first, that might be more relatable. Imagine that you are standing in front of a cave. 
"""


from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        def os_greedy2_cave():
            boxes.sort(reverse=True)
            i, count = 0, 0
            for r in warehouse:
                while i < len(boxes) and boxes[i] > r:
                    i += 1
                if i == len(boxes):
                    return count
                count += 1
                i += 1
            return count

        return os_greedy2_cave()


sl = Solution()
assert sl.maxBoxesInWarehouse(boxes=[4, 3, 4, 1], warehouse=[5, 3, 3, 4, 1]) == 3
print(sl.maxBoxesInWarehouse(boxes=[1, 2, 2, 3, 4], warehouse=[3, 4, 1, 2]))
