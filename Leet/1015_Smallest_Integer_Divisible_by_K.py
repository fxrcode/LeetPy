"""
✅ GOOD insight
💡 Pigeonhole Principle

Daily Challenge (Dec 30)
"""


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        def os_pigeon():
            """
            Runtime: 52 ms, faster than 68.07% of Python3 online submissions for Smallest Integer Divisible by K.

            T: O(K)
            """
            remainder = 0
            for n in range(1, k + 1):
                remainder = (remainder * 10 + 1) % k
                if remainder == 0:
                    return n
            return -1

        def os_slow():
            """
            Runtime: 61 ms, Your runtime beats 40.34 % of python3 submissions.

            """
            n = 1
            remainder = 1
            seen_remainder = set()
            while remainder % k != 0:
                x = remainder * 10 + 1
                remainder = x % k
                if remainder in seen_remainder:
                    return -1
                seen_remainder.add(remainder)
                n += 1
            return n


sl = Solution()
print(sl.smallestRepunitDivByK(3))
print(sl.smallestRepunitDivByK(17))
