'''
tag: medium
similar:
- 921: min insert
- 301: min remove

Lookback
- min swaps similar to 1247, find optimal strategy using semi-abstract case
'''

from collections import deque


class Solution:

    def minSwaps(self, s: str) -> int:

        def aayush912():
            """
            Runtime: 310 ms, faster than 99.06% of Python3 online submissions for Minimum Number of Swaps to Make the String Balanced.

            T: O(N)
            """
            l, r = 0, 0
            for c in s:
                if c == '[':
                    l += 1
                else:
                    if l > 0:
                        l -= 1
                    else:
                        r += 1
            return (l + 1) // 2

        def fxr_bfs():
            """
            TLE: 13 / 58 test cases passed.

            """

            def isval(s):
                l, r = 0, 0
                for c in s:
                    if c == '[':
                        l += 1
                    else:
                        if l > 0:
                            l -= 1
                        else:
                            r += 1
                return l, r

            if (0, 0) == isval(s):
                return 0
            seen = set([s])
            q = deque([s])
            swaps = 0
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    for i in range(len(s)):
                        for j in range(i + 1, len(s)):
                            if cur[i] == cur[j]:
                                continue
                            nei = list(cur)
                            nei[i], nei[j] = nei[j], nei[i]
                            nei = ''.join(nei)
                            if nei not in seen:
                                l, r = isval(nei)
                                if (l, r) == (0, 0):
                                    return swaps + 1
                                seen.add(nei)
                                q.append(nei)
                swaps += 1
            return -1

        # return fxr_bfs()
        return aayush912()


sl = Solution()
print(sl.minSwaps(s='][]['))
print(sl.minSwaps(s="]]][[["))
print(sl.minSwaps(s="[]"))
