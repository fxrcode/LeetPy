# Leetcode Explore Graph

- Oct 13 - Oct 15?
- https://leetcode.com/explore/featured/card/graph/

## Overview

- Graph is probably the data structure that has the closest resemblance to our daily life. There are many types of graphs describing the relationships in real life. For instance, our friend circle is a huge “graph”.

## Disjoint Set

- Overview of Disjoint Set
  - Given the vertices and edges between them, how could we quickly check whether two vertices are connected?
  - The primary use of disjoint sets is to address the connectivity between the components of a network. The “network“ here can be a computer network or a social network. For instance, we can use a disjoint set to determine if two people share a common ancestor.
- Two important functions of Disjoint Set
  - find
  - Union
- There are two ways to implement a “disjoint set”.

  - Quick Find: O(1) find, but O(N) union
  - Quick Union: more efficient than Quick Find.

- But both quick find/union are still bad.

  - How to do better? Ans: Union by Rank!
  - Here we define Rank: height of each vertex. Then we merge the shorter tree under the taller tree.
  - Now the union makes the tree balanced.
  - Optimized `union()`
  - Code:
    ```python
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    ```

- Path Compression Optimization

  - previously, notice that find() need to traverse the parent nodes sequentially until we reach the root node. If we call find(node_a) again, we repeat the same operations.
  - How to optimize the process? Ans: after finding the root, we can update the parent node of ALL traversed nodes to their root! In next time `find(node_a)`, the tree is flattened!
  - How to efficiently update the parent nodes of all traversed elements to the root?
    - ans: **RECURSION**!
  - This optimization is called "path compression", which optimizes the `find()` in **quick-union**.
    - The just one line change to origin quick-union by using **RECURSION**!
  - code:
    ```python
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    ```

- Tips for using the “disjoint sets” data structure in solving LeetCode problems
  - The code for the disjoint set is highly modularized. You might want to become familiar with the implementation. I would highly recommend that you understand and memorize the implementation of “disjoint set with path compression and union by rank”.
  - Finally, we strongly encourage you to solve the exercise problems using the abovementioned implementation of the “disjoint set” data structure. Some of these problems can be solved using other data structures and algorithms, but we highly recommend that you practice solving them using the “disjoint set” data structure.

## DFS in Graph

- Overview of DFS

  - Previously, we learned how to check connectivity between 2 vertices with UF.
  - Now let's switch gears and consider: Given a graph, how can we find all of its vertices, and how can we find all paths between two vertices?
    - DFS is ideal in solving these kind of problems since it explores all paths from the start vertex to all other vertices.
  - In Graphp theory, DFS is mainly used to
    1. Traverse all vertices in a "graph"
    2. Traverse all paths between any two vertices in a "graph"

- Eulerian path:
  - Hierholzer Algs: stepwise process to connect disjoint cycles (post order traversal )
- cycle detection
  - 3-color-variant DFS from CLRS
    - use color marking: WHITE (or None in Python) by default, GRAY for processing (in recursion tree), BLACK for processed (All decedents processed)
    - if visit a GRAY node, we got cycle. if visit a BLACK node, we got a Cross edge.

## BFS in Graph

- Shortest path in simple graph:
  - Although the `DFS` can find the shortest path between two vertices in a “graph” with equal and positive weights, it must traverse all paths between two vertices before finding the shortest one.
  - While `BFS`, in most cases, can find the shortest path without traversing all paths. This is because when using "breadth-first search", as soon as a path between the source vertex and target vertex is found, it is guaranteed to be the shortest path between the two nodes.

## MST

### Overview MST

- What is spanning tree?
  - A spanning tree is a connected subgraph in an undirected graph where all vertices are connected with the minimum number of edges.
- What is MST?
  - a spanning tree with the minimum possible total edge weight in a “weighted undirected graph”.
- In this chapter, we will learn about the “cut property and two algorithms for constructing a “minimum spanning tree”:

  - Kruskal’s Algorithm
  - Prim’s algorithm

### Cut property

- What is a “cut”? Although many theorems are named after people’s names, “cut” is not one of them. To understand the “cut property”, we need to understand two basic concepts.
  1. Cut: a “cut” is a partition of vertices in a “graph” into two disjoint subsets.
  2. Crossing Edge: a crossing edge is an edge that connects a vertex in one set with a vertex in the other set.
- Cut property: provides theoretical support for Kruskal and Prim algorithm.
  - For any cut `C` of the graph, if the weight of an edge `E` in the cut-set of `C` is strictly smaller than the weights of all other edges of the cut-set of `C`, then this edge belongs to all MSTs of the graph.

### Kruskal Algs:

1. Ascendign Sort all edges by their weight
2. Add edges in that order into MST. Skip the edges that would produce cycles int the MST.
3. Repeat step 2 until N-1 edges are added.

- Why does Kruskal’s Algorithm only choose N-1 edges?
  - Because Tree: E=V-1. Prove it by induction.
- Why can we apply the “greedy strategy”?
  - Proof by contradiction
- Complexity Analysis
  - T: O(ElogE), M: O(V)

### Prim Algs

- Video explain
- Proof of Prim Algs
- Difference between Kruskal vs Prim
  - `Kruskal` expands MST by adding **edges**.
  - `Prim` expands MST by adding **vertices**.
- Complexity Analysis
  - Time: O(ElogV) for binary heap
  - Space: O(V)

## SSSP

### Overview of SSSP

- BFS can only find shortest path in unweighted graph
- Why we need shortest path in weighted graph?

  - There're many routes from your home to target, say school. And the time for each routes may vary due to different time. The route with shortest distance may not be the one that requires least amount of time because of the speed limit and traffict jams.
  - Therefore the weight should be time instead of distance.
  - With that in mind, how to find shortest path given `TWO VERTICES` in a weighted graph?

- Edge Relaxation

  - Better think of relax as: imagine that each path is a rubber band of length 1 ![Imgur](https://imgur.com/DJqOXMt.png)

- In this chapter, we'll learn two SSSP algs:
  1. Dijkstra
  - can only be used to solve SSSP in weighted directed graph with `non-negative` weights
  2. Bellman-Ford
  - on the hand, can solve SSSP in weighted directed graph with `any` weights!

### Dijkstra SSSP

- The main idea

  - We take the starting point u as the center and gradually expand outward while updating the “shortest path” to reach other vertices.

  - “Dijkstra's Algorithm” uses a “greedy approach”. Each step selects the “minimum weight” from the currently reached vertices to find the “shortest path” to other vertices.

* Complexity
  - T: O(ElogV). M: O(V)

### Bellman-Ford SSSP

- Basic Theorem

  - Theorem 1: In a “graph with no negative-weight cycles” with N vertices, the shortest path between any two vertices has at most N-1 edges.
  - Theorem 2: In a “graph with negative weight cycles”, there is no shortest path.
    - XXX: Bellman-Ford can detect negative cycles!

- Naive Bellman-Ford

  - DP with N-1

- Optimized Bellman-Ford

  - if you just need to get Shortest Path between 2 nodes, then you can terminate earlier than N-1 once you found the table doesn't optimize compare to previous round.

- How to detect negative weight cycles?
  - Because Bellman will get SSSP in N-1 times, so if do the N-th time, and you get shorter than N-1, then it must be a negative weight cycle.

* Complexity
  - T: O(VE), M: O(V)

### Improved Bellman-Ford Algorithm with Queue — SPFA Algorithm

- TODO: Skip for now. I don't think Dijkstra & Bellman-Ford is good enough for FLAG.

## Kahn's Topological Sort

### Overview of Kahn's Algs

- Use BFS & In-degree to do toposort.
- Can also detect cycle.
- Limitation of the Algorithm
  - TopoSort only works with DAG
  - There must be at least one vertex with in-degree of 0.
