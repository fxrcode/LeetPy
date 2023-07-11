"""
https://github.com/stevenhalim/cpbook-code/blob/master/ch4/traversal/UVa11838.py
usage: 1192. Critical Connections in a Network


✅ GOOD Graph (SCC, fancy DFS)
💡insight
"""

import sys

UNVISITED = -1

dfsNumberCounter = 0
numSCC = 0
AL = []
AL_T = []
dfn = []
low = []
S = []
visited = []
st = []
# https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
sccs = []


def tarjanSCC(u):
    global low, dfn, dfsNumberCounter, visited
    global AL, numSCC, st
    global sccs

    low[u] = dfn[u] = dfsNumberCounter
    dfsNumberCounter += 1
    st.append(u)
    visited[u] = True

    # Consider successors of u
    for v in AL[u]:
        if dfn[v] == UNVISITED:
            tarjanSCC(v)
            # same as WilliamFiset, no need to update low here, since we use if rather elif!
        if visited[v]:
            low[u] = min(low[u], low[v])

    # If u is a root node, pop the stack and generate an SCC
    if low[u] == dfn[u]:
        numSCC += 1
        scc = []
        while True:
            v = st.pop()
            visited[v] = False
            scc.append(v)
            if u == v:
                sccs.append(scc)
                break


if __name__ == "__main__":
    # graph by: https://www.bilibili.com/video/BV19J411J7AZ
    with open("scc_in.txt") as f:
        V, E, s = map(int, f.readline().split(" "))
        AL = [[] for u in range(V)]
        for _ in range(E):
            u, v = map(int, f.readline().split(" "))
            AL[u].append(v)

        """ run Tarjan's SCC code here """
        dfn = [UNVISITED] * V
        low = [0] * V
        visited = [False] * V
        st = []
        dfsNumberCounter = 0
        numSCC = 0
        for u in range(V):
            if dfn[u] == UNVISITED:
                tarjanSCC(u)
        print(low, numSCC)
        print(sccs)
