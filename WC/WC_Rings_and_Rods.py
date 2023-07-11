class Solution:
    def countPoints(self, rings: str) -> int:
        r2c = {i: set() for i in range(10)}
        for i in range(0, len(rings), 2):
            c, r = rings[i], int(rings[i + 1])
            r2c[r].add(c)
        ans = []
        print(r2c)
        for r, c in r2c.items():
            if len(c) == 3:
                ans.append(r)
        return len(ans)
