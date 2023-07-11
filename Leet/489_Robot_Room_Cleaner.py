"""
✅ GOOD Backtrack (2D Matrix)

https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2794/
Leetcode explore Recursion II: Backtracking

You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.


"""
"""
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
"""


class Robot:
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """


class Solution:
    def cleanRoom(self, robot):
        """
        Runtime: 119 ms, faster than 15.07% of Python3 online submissions for Robot Room Cleaner.

        T: O(4*(N-W)), M: O(N-W) # N is number of cells in room, W is number of obstracles
        We visit each non-obstackle cell once and only once, at each visit, we check 4 directions around the cell.
        """
        # URDL. The order is important. Why start from U? A: initial direction of robot is UP.
        DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def goback():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def bt(x, y, d):
            """
            Why x,y,d? because this describe the state in recursion tree
            After each recursion call, it cleaned up all reachable cells

            XXX: careful there're 2 state change: cell to next cell, and robot move to next pos.
                the (x,y)->(xx,yy) is next cell, and robot.move(), robot.turnRight moves robot to next pos.
                goback backtrack stae upper level (above for, aka: (x,y,d)

            XXX: as Geeta's Algorithms Huddles: Robot Room Cleaner DFS Solution
                backtrack makes the DFS recursion -> NOOPS.
                loc is small, the essence is to grasp DFS/backtracking concept
            """
            visited.add((x, y))
            robot.clean()

            for i in range(4):
                nd = (d + i) % 4
                dx, dy = DIR[nd]
                xx, yy = x + dx, y + dy
                # recurive if not visit and reachable
                if (xx, yy) not in visited and robot.move():
                    bt(xx, yy, nd)
                    # backtrack to (x,y), with origin direction
                    goback()

                # now at (x,y) with d, update direction (clockwise)
                robot.turnRight()

        bt(0, 0, 0)
