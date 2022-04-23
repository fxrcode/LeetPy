'''
💡insight (Find pattern by simulation)
Daily Challenge (Jan 9)
'''


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def fxr():
            """
            Runtime: 24 ms, faster than 96.05% of Python3 online submissions for Robot Bounded In Circle.

            T: O(N)
            similar: 489. Robot Room Cleaner

            """
            x, y = 0, 0
            DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # north
            d = 0
            for ins in instructions:
                if ins == 'G':
                    dx, dy = DIR[d]
                    x, y = x + dx, y + dy
                elif ins == 'L':
                    d = (d - 1) % 4
                else:
                    d = (d + 1) % 4
            if x == y == 0 or d != 0:
                return True
            return False

        return fxr()


sl = Solution()
print(sl.isRobotBounded(instructions="GGLLGG"))
print(sl.isRobotBounded(instructions="GG"))
print(sl.isRobotBounded(instructions="GL"))
print(sl.isRobotBounded("GLRLLGLL"))
