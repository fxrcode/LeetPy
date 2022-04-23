'''
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1136/
Leetcode Explore: Hash Table. Conclusion

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
'''


class Solution:
    def numJewelsInStones_lee215(self, jewels: str, stones: str) -> int:
        sj = set(jewels)
        # What this? Ans: generator_expressions, returns T/F, so we can sum.
        gen_exp = (c in sj for c in stones)
        return sum(gen_exp)

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Your runtime beats 87.16 % of python3 submissions.
        T: O(J+S), M: O(J)

        XXX: the problem for me is take time to understand what the problem mean.
        Only understand after read leetcode-cn: https://leetcode-cn.com/problems/jewels-and-stones/solution/hua-jie-suan-fa-771-bao-shi-yu-shi-tou-by-guanpeng/
        * each char in jewels represent a type of jewel.

        """
        sj = set(jewels)
        ans = 0
        for c in stones:
            if c in sj:
                ans += 1
        return ans


sl = Solution()
print(sl.numJewelsInStones_lee215('aA', 'aAAbbbb'))
