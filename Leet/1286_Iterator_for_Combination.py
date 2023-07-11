"""
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

NOTE: Daily LeetCoding Challenge November, Day 14
✅ GOOD DFS, Bitmask, Algorithm L
✅ GOOD Logic

Metacognition: the brute force is to precompution all combinations, so standard backtracking.
* But it's quite similar to next permutation: Back to back SWE!!! So simply swap and reverse?
* Actually DBabichev followed this route: https://leetcode.com/problems/iterator-for-combination/discuss/790113/Python-O(k)-on-the-fly-explained
* And Huifeng Guan is more straightforward: https://www.youtube.com/watch?v=KzeHp5Xyp28

OS: 5 Solutions: Bitmasking + Algorithm L (Knuth!!!)
"""


class CombinationIterator:
    """
    Runtime: 48 ms, faster than 84.82% of Python3 online submissions for Iterator for Combination.

    https://leetcode.com/problems/iterator-for-combination/discuss/789649/Python-2-solutions-with-explanations
    XXX: beautiful iterative on-fly combination generator (similar to Knuth Algorithm L) by nikryl
    """

    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.k = k = combinationLength
        self.n = len(self.s)
        self.comb = [i for i in range(k - 1)] + [k - 2]
        print(self.comb)

    def next(self) -> str:
        """
        XXX: Beautiful logic! Feels similar to Knuth Algorithm L
        """
        for i in range(1, self.k + 1):
            if self.comb[-i] < self.n - i:
                self.comb[-i] += 1
                while i != 1:
                    self.comb[-i + 1] = self.comb[-i] + 1
                    i -= 1
                break

        cmb = "".join([self.s[pos] for pos in self.comb])
        cmbbit = "".join(map(str, self.comb))
        print(cmb, cmbbit)
        return cmb

    def hasNext(self) -> bool:
        return self.comb[0] != self.n - self.k


class CombinationIterator_bitmask:
    """
    Runtime: 91 ms, faster than 7.86% of Python3 online submissions for Iterator for Combination.

    OS: just very naive/straightforward impl... So it's sloooow
    """

    def __init__(self, characters: str, combinationLength: int):
        self.n = n = len(characters)
        self.k = k = combinationLength
        self.chars = characters

        # generate first bitmask 1(k)0(n - k)
        self.b = (1 << n) - (1 << n - k)

    def next(self) -> str:
        # convert bitmasks into combinations
        # 111 --> "abc", 000 --> ""
        # 110 --> "ab", 101 --> "ac", 011 --> "bc"
        curr = [self.chars[j] for j in range(self.n) if self.b & (1 << self.n - j - 1)]

        # generate next bitmask
        self.b -= 1
        while self.b > 0 and bin(self.b).count("1") != self.k:
            self.b -= 1

        ans = "".join(curr)
        print(ans)
        return ans

    def hasNext(self) -> bool:
        return self.b > 0


class CombinationIterator_os_algoL_precompute:
    """[summary]
    OS said: Algorithm L is an efficient BFS that generates one by one the combinations of indexes.
    But I was like: ¯\_(ツ)_/¯
    """

    def __init__(self, characters: str, combinationLength: int):
        self.combis = []
        n, k = len(characters), combinationLength

        # init the first combination
        nums = list(range(k)) + [n]

        j = 0
        while j < k:
            # add current combination
            cur = [characters[n - 1 - nums[i]] for i in reversed(range(k))]
            self.combis.append("".join(cur))

            # generate next combination,
            # find first j s.t. nums[j] +1 != nums[j+1]
            # increase nums[j] by one
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j
                j += 1
            nums[j] += 1

    def next(self) -> str:
        ret = self.combis.pop()
        print(ret)
        return ret

    def hasNext(self) -> bool:
        return self.combis

    """
    def combi(start, path, res):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, len(characters)):
            combi(i+1, path+[characters[i]], res)
    """


"""
"""
# os_algoL_precomp = CombinationIterator('abcdefg', 4)
os_algoL_precomp = CombinationIterator("abc", 2)
while os_algoL_precomp.hasNext():
    os_algoL_precomp.next()
