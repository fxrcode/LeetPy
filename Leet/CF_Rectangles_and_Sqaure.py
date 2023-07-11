"""
Google interview: given a list of rectangles, can you use a subset or all of them to tile a sqaure? Retrun bool.
How are you going to represent the rectangle object? Since the question is verbal with open design

Ref: 1240. Tiling a Rectangle with the Fewest Squares
     Codeforces 335D Rectangles and Square 暴力+ DP

TODO: I implemented backtracking to try all subsets of rectangles for a square.
FOLLOWUP: you can reuse rectangles or cut large rectangle to smaller one.
"""


class RectangleSquare:
    def drive(self, rectangles) -> bool:
        """
        Args:
            rectangles (List[(r,c)]):
        """
        row_sum, col_sum = 1, 1
        for rec in rectangles:
            row_sum += rec[0]
            col_sum += rec[1]
        square_max = min(row_sum, col_sum)
        for s in range(1, square_max + 1):
            sqr = [[0 for _ in range(s)] for _ in range(s)]
            pass
        return False

    @staticmethod
    def search(sqr, rect):
        # return ALL cord of left-up cornor to put the rect, if not found, return []
        def all_0(sqr, r, c, r_end, c_end):
            for i in range(r, r_end + 1):
                for j in range(c, c_end + 1):
                    if sqr[i][j] != 0:
                        return False
            return True

        res = []
        S = len(sqr)
        rec_r, rec_c = rect
        for r in range(S):
            for c in range(S):
                r_end = r + rec_r - 1
                c_end = c + rec_c - 1
                if r_end < S and c_end < S and all_0(sqr, r, c, r_end, c_end):
                    res.append((r, c))
        return res

    @staticmethod
    def update_sqr(sqr, bit, r, c, r_end, c_end):
        # set rectangle in sqr to bit (eg. 0->1), and area: [r,r_end] & [c,c_end] all inclusive
        for i in range(r, r_end + 1):
            for j in range(c, c_end + 1):
                if sqr[i][j] == bit:
                    raise Exception(f"{(i,j)} is alraedy equal to bit {bit}")
                sqr[i][j] = bit

    @staticmethod
    def all_marked(sqr):
        S = len(sqr)
        for i in range(S):
            for j in range(S):
                if sqr[i][j] == 0:
                    return False
        return True

    @staticmethod
    def plot_sqr(sqr):
        S = len(sqr)
        for i in range(S):
            for j in range(S):
                if sqr[i][j] == 0:
                    print(".", end="")
                else:
                    print("x", end="")
            print()
        print()

    def backtrack(self, sqr, rectangles, startIdx, path, ans) -> bool:
        """
        path: i-th rectangle at (r,c)
        """

        if RectangleSquare.all_marked(sqr):
            print("++++++++++++++++++++ BINGO ++++++++++++++++++++++++")
            for k, v in path.items():
                ans.append((k, v))
            # XXX: Stop recursion once we got 1 solution: https://github.com/jiajunhua/labuladong-fucking-algorithm
            return True

        # if idx == len(rectangles):
        #     return False

        # BUG, XXX: I didn't use loop to try all idx and I debug for so long!!!
        #   the reason that my bug didn't show up in some case, this is actually a once leg search, rather complete search.
        #   eg. rectangles = [(1, 2), (2, 2)] for square 2 doesn't work, because it's always from (1,2) due to one-leg!
        for i in range(startIdx, len(rectangles)):
            # search ALL space in sqr that can fit rectangles[idx]
            opt_coords = RectangleSquare.search(sqr, rectangles[i])

            if not opt_coords:
                print(f"cant fit rectangle {i}: {rectangles[i]} in sqr, try next rect")
                # try next
                if self.backtrack(sqr, rectangles, i + 1, path, ans):
                    return True

            else:
                print(f"before pick: {i}")
                RectangleSquare.plot_sqr(sqr)
                print(f"try rectangle {i}: {rectangles[i]} at {opt_coords}")
                # for cord in searched space, make decision
                for coord in opt_coords:
                    r, c = coord
                    print(f"pick rec {i}: {rectangles[i]} to put at {(r,c)}")
                    r_end, c_end = r + rectangles[i][0] - 1, c + rectangles[i][1] - 1
                    #   update sqr to mark the rectangle part to 1, and update path
                    RectangleSquare.update_sqr(sqr, 1, r, c, r_end, c_end)
                    RectangleSquare.plot_sqr(sqr)
                    path[i] = (r, c)
                    #   recursive to try next rectangle
                    if self.backtrack(sqr, rectangles, i + 1, path, ans):
                        # XXX: Stop recursion once we got 1 solution: https://github.com/jiajunhua/labuladong-fucking-algorithm
                        return True
                    #   backtrack the marked part to 0, undo path update
                    RectangleSquare.update_sqr(sqr, 0, r, c, r_end, c_end)
                    del path[i]
                    print(f"remove rec {i}: {rectangles[i]} at {(r,c)} ")
                    RectangleSquare.plot_sqr(sqr)

    """
    BUG: I didn't use loop to try all idx and I debug for so long!!! eg. failed for rectangles = [(1, 2), (2, 2), ]
    def backtrack(self, sqr, rectangles, idx, path, ans) -> bool:
        # path: i-th rectangle at (r,c)

        if CompleteSearch01.all_marked(sqr):
            print("++++++++++++++++++++ BINGO ++++++++++++++++++++++++")
            for k, v in path.items():
                ans.append((k, v))
            # XXX: Stop recursion once we got 1 solution: https://github.com/jiajunhua/labuladong-fucking-algorithm
            return True

        if idx == len(rectangles):
            return False
        # search ALL space in sqr that can fit rectangles[idx]
        opt_coords = CompleteSearch01.search(sqr, rectangles[idx])

        if not opt_coords:
            print(
                f'cant fit rectangle {idx}: {rectangles[idx]} in sqr, try next rect')
            # try next
            if self.backtrack(sqr, rectangles, idx+1, path, ans):
                return True

        else:
            print(f'before pick: {idx}')
            CompleteSearch01.plot_sqr(sqr)
            print(f'try rectangle {idx}: {rectangles[idx]} at {opt_coords}')
            # for cord in searched space, make decision
            for coord in opt_coords:
                r, c = coord
                print(f'pick rec {idx}: {rectangles[idx]} to put at {(r,c)}')
                r_end, c_end = r + \
                    rectangles[idx][0] - 1, c+rectangles[idx][1]-1
                #   update sqr to mark the rectangle part to 1, and update path
                CompleteSearch01.update_sqr(sqr, 1, r, c, r_end, c_end)
                CompleteSearch01.plot_sqr(sqr)
                path[idx] = (r, c)
                #   recursive to try next rectangle
                if self.backtrack(sqr, rectangles, idx+1, path, ans):
                    # XXX: Stop recursion once we got 1 solution: https://github.com/jiajunhua/labuladong-fucking-algorithm
                    return True
                #   backtrack the marked part to 0, undo path update
                CompleteSearch01.update_sqr(sqr, 0, r, c, r_end, c_end)
                del path[idx]
                print(f'remove rec {idx}: {rectangles[idx]} at {(r,c)} ')
                CompleteSearch01.plot_sqr(sqr)
    """


def build_sqr(s):
    sqr = [[0 for _ in range(s)] for _ in range(s)]
    return sqr


sl = RectangleSquare()
# rectangles = [(2, 1), (1, 1), (1, 2), (3, 1), (2, 1)]
# rectangles = [(3, 1), (2, 1), (1, 1), (2, 2), (3, 1), (1, 2)]
rectangles = [
    (1, 2),
    (2, 2),
]
ans = []
sl.backtrack(build_sqr(2), rectangles, 0, {}, ans)
print(ans)
