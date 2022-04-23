# Classic problems

- collect common problems as my handbook/template

## DP

### Classics

- Coin change problem - `O(nW)`
- Edit distance - `O(nm)`
- Knapsack 0/1 - `O(nW)`
- Maximum contiguous subarray - `O(n)`
- Longest Common Subsequence (LCS) - `O(nm)`
- Longest Increasing Subsequence (LIS) - `O(n2)`
- Longest Palindrome Subsequence (LPS) - `O(n2)`
- Traveling Salesman Problem (dynamic programming) - `O(n^2 * 2^n)`
- Minimum Weight Perfect Matching (iterative, complete graph) - `O(n^2 * 2^n)`

### Examples

- Tiling Dominoes

## Graph

### Trees

- Rooting an undirected tree - `O(V+E)`
- Identify isomorphic trees - `O(?)`
- Tree centers - `O(V+E)`
- Tree diameter - `O(V+E)`
- LCA

### Main graph theory algs

- Bellman-Ford (adjancy matrix, negative cycles) - `O(V^3)`
- BFS - `O(V+E)`
- Bridges/cut edges - `O(V+E)`
- Find connected components (UF) - `O(ElogE)`
- Find connected components (DFS) - `O(V+E)`
- DFS - `O(V+E)`
- 3-color-variant DFS (detect cycle) - `O(V+E)`
- Dijkstra SSSP (lazy pq) - `O(ElogV)`
- Eulerian Path (directed graph) - `O(E+V)`
- Floyed Warshall algs (negative cycle check) - `O(V^3)`
- Graph diameter - `O(VE)`
- Kahn's Topological sort - `O(V+E)`
  - ie. Longest Path in DAG (329. Longest Increasing Path in a Matrix)
- Kruskal MST (UF) - `O(ElogE)`
- Prim MST () - `O(ElogV)`
  - Dijkstra and Prim. The main difference is here: for Prim `graph[u][v] < key[v]`, and for Dijkstra `dist[u]+graph[u][v] < dist[v]`. So as you can see from the graphs in those two pages, they are different mainly because of these two lines of code. [SOF](https://stackoverflow.com/questions/14144279/difference-between-prims-and-dijkstras-algorithms)

## Geometry

- Closest pair of points (sweeping line) - O(nlog(n))

## Backtracking

- n-queen problem:O(n!)
- graph coloring problem:O(nm^n) (where n=#vertex,m=#color used)
- Hamiltonian cycle:O(N!)
- WordBreak and StringSegment:O(2^N)
- subset sum problem:O(nW)

## REF

- [WilliamFiset](https://github.com/williamfiset/Algorithms/blob/master/README.md)
- [来和大家聊聊我是如何刷题的（第一弹）](https://segmentfault.com/a/1190000038379982)
  - 另外插一句题外话， LIS 真的很有用，大家一定要掌握，掌握了平方的解法再去看看 $NlogN$ 的解法，一些 HARD 题目必须要 $NlogN$ 才能过。
- [从零到谷歌程序员: 550 道题(150+310+90)](https://zhuanlan.zhihu.com/p/394297179)
  - 对于前 200 和一些高频题，我刷了两遍以上或者更多。
