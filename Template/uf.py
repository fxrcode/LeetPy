class UF:
    """
    REF: https://cs.stackexchange.com/a/128230
    neat UF, similar to algs4, union-by-size is neater than union-by-rank,
        since rank is virtual concept, but size maybe needed for query,
        so we don't need to maintain both size & rank
    """

    def __init__(self, n) -> None:
        self.cnt = n
        self.root = list(range(n))
        self.sz = [1] * n

    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]

    def union(self, i, j):
        x, y = map(self.find, [i, j])
        if x == y:
            return
        if self.sz[x] > self.sz[y]:
            x, y = y, x
        self.root[x] = y
        self.sz[y] += self.sz[x]
        self.cnt -= 1

    def count(self):
        return self.cnt

    def connected(self, i, j):
        return self.find(i) == self.find(j)


edges = [[0, 1], [1, 2], [3, 4]]
uf = UF(n=5)
for x, y in edges:
    uf.union(x, y)

# https://www.geeksforgeeks.org/getter-and-setter-in-python/
# Python's field is not same as other OOP PL. So you can directly get/set it rather implement getter/setter.
print(uf.root)
print(uf.cnt)
print(uf.sz)
