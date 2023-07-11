"""
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1177/
Leetcode Explore: Hash Table. Practical Application - HashMap
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.


"""


from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        Your runtime beats 40.18 % of python3 submissions.

        https://leetcode.com/problems/minimum-index-sum-of-two-lists/discuss/103745/Python-Straightforward-with-Explanation
        Use dict.get(key, 1e6), this 1e6 unified found, and missing restaurant in list2 calculation
        T: O(n+m), M: O(min(m,n))
        """
        d = {n: i for i, n in enumerate(list1)}
        mn_sum, ans = 1e6, []
        for i, n in enumerate(list2):
            # BUG ia = d.get(n, 1000) this will lead to WRONG answer! Hard to distinguish found/missing!
            ia = d.get(n, 1e6)
            if ia + i < mn_sum:
                mn_sum = ia + i
                ans = [n]
            elif ia + i == mn_sum:
                ans.append(n)
        return ans

    def findRestaurant_WRONG(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        my 1st attempt is WRONG!
        """
        d = {}
        for i, r in enumerate(list1):
            if r not in d:
                d[r] = i
        for i, r in enumerate(list2):
            # BUG: This d[r] add can't distringuish found vs missing!
            if r in d:
                d[r] += i
        print(d)
        res = [(he, res) for res, he in d.items()]
        res.sort(key=lambda tu: tu[0])
        return [tu[1] for tu in res]


sl = Solution()
# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["Piatti", "The Grill at Torrey Pines",
#          "Hungry Hunter Steakhouse", "Shogun"]

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]
print(sl.findRestaurant(list1, list2))
