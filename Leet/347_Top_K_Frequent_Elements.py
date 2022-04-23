'''
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1133/
Leetcode Explore: Hash Table. Conclusion

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

'''


from typing import List
from collections import Counter, defaultdict
from heapq import heapify, heappush, heappop, heappushpop
from random import randint


class Solution:
    def topKFrequent_hoare_select(self, nums: List[int], k: int) -> List[int]:
        """
        Your runtime beats 99.86 % of python3 submissions.

        k-th somethings pattern: use Hoare linear selection
        Time: O(N), Space: O(N)
        """
        def partit(nums, l, r):
            # in-place action, partition nums[l:r]
            # pick a random pivot index, then move it to the ned
            ri = randint(l, r)
            # ri = r
            pivot = nums[ri]
            nums[ri], nums[r] = nums[r], nums[ri]

            # lomuto
            s = l-1
            # loop invariant: [0,s] < pivot
            for f in range(l, r):
                # if nums[f] < pivot:
                if nums[f][1] < pivot[1]:
                    s += 1
                    nums[s], nums[f] = nums[f], nums[s]
            # swap
            nums[s+1], nums[r] = nums[r], nums[s+1]
            return s+1

        # print(partit(nums, 0, len(nums)-1))

        def quick_select(nums, l, r, k) -> int:
            if l == r:
                return nums[l]
            pi = partit(nums, l, r)
            if k == pi:
                return nums[k]
            elif k < pi:
                return quick_select(nums, l, pi-1, k)
            else:
                return quick_select(nums, pi+1, r, k)

        # for k in range(len(nums)):
        #     print(quick_select(nums, 0, len(nums)-1, k))
        # quick_select(nums, 0, len(nums)-1, len(nums)-k)
        # return nums[len(nums)-k:]
        ctr = Counter(nums)

        # XXX: don't use freq2nums dict since it makes collecting top-k freq not that straight.
        #       instead, I simply augment the default lomuto partition template by comparing pivot's freq!
        #       because n2f is list of tuple(num, freq), which is simple to quick-select.
        n2f = list(ctr.items())

        res = []
        for i in range(len(n2f)-1, len(n2f)-k-1, -1):
            res.append(n2f[i][0])
        return res

    def topKFrequent_minheap(self, nums: List[int], k: int) -> List[int]:
        """
        Runtime: 96 ms, faster than 90.27% of Python3 online submissions for Top K Frequent Elements.

        counter: O(N) T/M
        minheap: T: O(klogk)+O((N-k)logk)=>O(Nlogk), M: O(k)

        So total T: O(N), space O(N+k)
        """
        ctr = Counter(nums)

        pq = []  # XXX: minheap for top-K, or maxheap for bottom-K
        for n, f in ctr.items():
            if len(pq) < k:
                heappush(pq, (f, n))
                continue
            # BUG: mn_f, mn_n = heappop(pq)
            mn_f, mn_n = pq[0]
            if mn_f <= f:
                heappushpop(pq, (f, n))

        res = [n for f, n in pq]
        return res

    def topKFrequent_simple_pq(self, nums: List[int], k: int) -> List[int]:
        """
        Runtime: 96 ms, faster than 90.27% of Python3 online submissions for Top K Frequent Elements.
        Counter: O(N) T/M
        maxheap: O(nlogn+k)

        XXX: study heapq:
        1) I didn't know that heappush/heappop just maintain heapq invariant.
            But it's required that the 1st arg of heappush/heappop must be already fulfil heappq invariant.
            So you have to heapify(pq) before heappush(pq, item)/heappop(pq).
        2) heapify(pq) is in-place, so no output! same as list.sort().
        """
        ctr = Counter(nums)
        # pq = heapify([(-f, n) for n, f in ctr.items()])
        pq = [(-f, n) for n, f in ctr.items()]
        heapify(pq)
        res = []
        for _ in range(k):
            nf, n = heappop(pq)
            res.append(n)
        return res

    def topKFrequent_WRONG(self, nums: List[int], k: int) -> List[int]:
        """
        WA in 1st try. Because I gorup nums by same freq!
        eg. nums=[1,2], k = 2. I got only 1 element in priorityqueue!
        """
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        freq2nums = defaultdict(list)
        # XXX: for k,v in counter.items(): I accidentially overwrite argument k!
        for n, f in counter.items():
            freq2nums[f].append(n)
        maxheap = []

        # XXX: to loop, key,val of dict, always remember to use dict.items()!
        # Ow. You'll justs loop key rather k,v by `for kv in dict`!
        for f, nums in freq2nums.items():
            heappush(maxheap, (-f, nums))

        print(freq2nums)
        res = []
        for _ in range(k):
            f, nums = heappop(maxheap)
            print(-f, nums)
            res.extend(nums)
        return res


sl = Solution()
# print(sl.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
# print(sl.topKFrequent(nums=[3, 0, 1, 0], k=1))
# print(sl.topKFrequent_hoare_select(nums=[4, 1, 9, 5, 14, 6, 6], k=7))
print(sl.topKFrequent_hoare_select(nums=[1, 1, 1, 2, 2, 3], k=3))
