'''
✅ GOOD Logic
Daily Challenge (01212022, 01072023)
[ ] REDO
'''

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def optim():
            """
            Runtime: 564 ms, faster than 41.33% of Python3 online submissions for Gas Station.

            https://leetcode.com/problems/gas-station/discuss/1706142/JavaC%2B%2BPython-An-explanation-that-ever-EXISTS-till-now!!!!

            T:O(N)
            """
            start, total_tank, cur_tank = 0, 0, 0
            for i in range(len(gas)):
                total_tank += gas[i] - cost[i]
                cur_tank += gas[i] - cost[i]
                if cur_tank < 0:
                    start = i + 1
                    cur_tank = 0
            return start if total_tank >= 0 else -1

        return optim()

        def simulation():
            """
            https://leetcode.com/problems/gas-station/discuss/1706142/JavaC%2B%2BPython-An-explanation-that-ever-EXISTS-till-now!!!!

            T:O(N^2)
            """
            n, total = len(gas), 0
            for i in range(n):
                total = 0
                stops = 0
                j = i
                while stops < n:
                    total += gas[j % n] - cost[j % n]
                    if total < 0: break
                    stops += 1
                    j += 1
                if stops == n and total >= 0: return i
            return -1

        '''
        def fxr():
            """
            if x -> z failed, then k in (x,z) can't. So We can directly try z
            """
            def travel(start):
                x = start
                g = gas[x]
                while x < start + N:
                    x_1 = x + 1
                    if g - cost[x % N] < 0:
                        x = x_1
                        return -(x % N)
                    else:
                        g = g - cost[x % N] + gas[x_1 % N]
                        x = x_1
                return x

            N = len(gas)
            i = 0
            while i < N:
                x = travel(i)
                if x > 0:
                    return i
                else:
                    i = -x
            return i
        '''


sl = Solution()
print(sl.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
print(sl.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
