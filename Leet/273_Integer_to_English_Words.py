"""
tag: Hard, Amazon
Lookback:
- recursion skills and prepare for a bit long CONSTANT init
- Python slicing invalid index handling is COOL
- Good for bar raiser to make you stress and pressure
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        def pochmann_recursive():
            """
            Runtime: 60 ms, faster than 22.44% of Python3 online submissions for Integer to English Words.

            https://leetcode.com/problems/integer-to-english-words/discuss/70632/Recursive-Python
            """
            to19 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
            tens = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
            bigs = {10**9: "Billion", 10**6: "Million", 1000: "Thousand"}

            def words(n):
                if n < 20:
                    #! hidden gem: auto handle n=0, so [n-1:n] is invalid => []
                    # BUG: return [to19[n-1]], failed for n=0, this returns Nineteen!
                    return to19[n - 1 : n]
                elif n < 100:
                    return [tens[n // 10 - 2]] + words(n % 10)
                elif n < 1000:
                    return [to19[n // 100 - 1]] + ["Hundred"] + words(n % 100)
                else:
                    for i in bigs:
                        if n // i > 0:
                            return words(n // i) + [bigs[i]] + words(n % i)

            return " ".join(words(num)) or "Zero"

        return pochmann_recursive()


sl = Solution()
nums = [0, 123, 12345, 1234567]
for n in nums:
    print(sl.numberToWords(n))
