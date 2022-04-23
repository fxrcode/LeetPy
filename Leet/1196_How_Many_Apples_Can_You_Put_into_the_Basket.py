'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''


from typing import List
import heapq


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        def os_bucket_sort():
            """
            Runtime: 118 ms, faster than 26.71% of Python3 online submissions for How Many Apples Can You Put into the Basket.

            T: O(N+W), M: O(W). N is # of weight, W is max(weight)
            """
            size = max(weight)+1
            bucket = [0] * size
            for w in weight:
                bucket[w] += 1

            apples, money = 0, 5000
            for w in range(size):
                if bucket[w] != 0:
                    take = min(bucket[w], money//w)
                    if take == 0:
                        break
                    apples += take
                    money -= w * take
            return apples

        def os_greedy_heap():
            """
            Runtime: 156 ms, faster than 15.22% of Python3 online submissions for How Many Apples Can You Put into the Basket.

            T: O(N + klogN), M: O(N)
            XXX: heapify(x) transforms list x into a heap, in-place, in linear time.
            """
            heapq.heapify(weight)
            money = 5000
            apples = 0
            while weight and money - weight[0] >= 0:
                apples += 1
                money -= heapq.heappop(weight)
            return apples

        def fxr_greedy():
            """
            Runtime: 221 ms, faster than 5.28% of Python3 online submissions for How Many Apples Can You Put into the Basket.

            T: O(nlogn)
            """
            weight.sort()
            hold, cost = 0, 5000
            for w in weight:
                if cost - w >= 0:
                    print(cost, w)
                    hold += 1
                    cost -= w
            return hold

        # return fxr_greedy()
        # return os_greedy_heap()
        return os_bucket_sort()


sl = Solution()
print(sl.maxNumberOfApples([988, 641, 984, 635, 461, 527, 491, 610, 274, 104, 348, 468, 220, 837, 126, 111, 536, 368, 89, 201, 589, 481,
      849, 708, 258, 853, 563, 868, 92, 76, 566, 398, 272, 697, 584, 851, 302, 766, 88, 428, 276, 797, 460, 244, 950, 134, 838, 161, 15, 330]))
