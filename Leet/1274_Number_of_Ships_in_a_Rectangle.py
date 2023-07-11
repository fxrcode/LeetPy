"""
Weekly Special (W2 Feb2022)
tag: hard? Divide-conquer
"""


class Sea(object):
    def hasShips(self, topRight: "Point", bottomLeft: "Point") -> bool:
        pass


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Solution(object):
    def countShips(self, sea: "Sea", topRight: "Point", bottomLeft: "Point") -> int:
        def count(sea: "Sea", P: Point, Q: Point):
            """
            Runtime: 53 ms, faster than 64.52% of Python3 online submissions for Number of Ships in a Rectangle.

            XXX: https://leetcode.com/problems/number-of-ships-in-a-rectangle/discuss/440773/python-divide-and-conquer-with-picture-explanation
            Note mx+1 vs mx for different quadrant
            ![](../pics/1274_Quad.png)

            draw ascii table: https://ozh.github.io/ascii-tables/
            +---+---+
            | 2 | 1 |
            +---+---+

            +---+---+
            | 3 | 4 |
            +---+---+
            """
            res = 0
            if P.x >= Q.x and P.y >= Q.y and sea.hasShips(P, Q):
                if P.x == Q.x and P.y == Q.y:
                    return 1
                mx, my = (P.x + Q.x) // 2, (P.y + Q.y) // 2
                f1 = count(sea, P, Point(mx + 1, my + 1))
                f2 = count(sea, Point(mx, P.y), Point(Q.x, my + 1))
                f3 = count(sea, Point(mx, my), Q)
                f4 = count(sea, Point(P.x, my), Point(mx + 1, Q.y))
                res = f1 + f2 + f3 + f4
            return res

        return count(sea, topRight, bottomLeft)
