# Queue & Stack (Sep 16)

- https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1355/
- Sep 8, 2021 -> Sep 22, 2021

## Queue: FIFO

## Queue and BFS

- It will be important to determine the nodes and the edges before doing BFS in a specific question.

  - Typically, the node will be an actual node or a status while the edge will be an actual edge or a possible transition.

- Classic BFS
  1. Number of Islands
     - connected components is classic of UF and BFS
  2. Open the lock
     - BFS is class complete search strategy to enumerate all potential solutions
  3. Perfect squares
     - After 1 week, already forgot how to write BFS!!!
     - tried DP recursive/iterative, both TLE.

## Stack: LIFO

- Min Stack
  - AC after I saw the given hint #1: store curMin in node when push. (Augmented data structure!)

* Valid Parantheses

  - AC because I already know from labuladong.

* Daily Temperatures

  - AC after I review labuladong ch 3.7.1 Mono-Stack. Get better understanding in code.

* Evaluate Reverse Polish Notation
  - simple stack. Just be careful on python div. eg. `1//-132=>-1`. Work around: `int(1/-132)`

## Stack and DFS

- Stack and DFS

  - The gif is important to fully understand the implicit stack during DFS
    - traverse till the deepest, then trace back in call-stack.
    - After we found target and return, it just return from that call. Still need to trace back the call-stack and pop all the call until call-stack is empty.
    - Here's just one of the slide: ![](../../assets/leet-explore-stack-dfs-1.png)
    - As a result, the first path you found in DFS is not always the shortest path, eg, in here, we found A-C-F-G, rather A-D-G.
    - Also, in graph, we need `visited[]` so C will not revisit E.

  * What is the push/pop order of the stack?
    - The processing order of the nodes is the exact opposite order as how they were added to the stack, which is Last-in-First-out (LIFO). That's why we use a `stack` in DFS.

- DFS - Template I

  - Here's the common recursive DFS, easy to code.

  ```python
  dfs(cur: Node, target: Node, visited: Set[Node])->bool:
    if cur == target:
      return True
    for next in neighbors(cur):
      if next not in visited:
        visited.add(next)
        if dfs(next, target, visited):
          return True
    return False
  ```

- Number of Islands

  - Damn, I forgot DFS...
  - Repeat, Repeat, Repeat! Then you'll understand algorithms.

- Clone graph
  [x] Study Graph DFS template

- Target Sum

  - Classic problem for Backtracking vs DP (Labuladong CH 2.19)
  - lee215 use 2 dict to implement level-order BFS

- DFS - Template II

  - Recursion is easier and intuitive to implement, but may SOF due to depth of recursion stack.
  - In that case, the solution is BFS or explicit Stack DFS

  * DFS with explicit stack

  ```python
  dfs(root, target)->bool:
    visited = set()
    stk = [root]
    while stk:
        cur = stk.pop()
        if cur == target:
           return True
          for neig in cur.neighbors:
            if neig not in visited:
              visited.add(neig)
              stk.append(visited)
    return False
  ```

  - The logic is exactly the same with recursion solution. But we use while loop and stack to simulate system call stack during recursion.
  - You'd better run through several examples manually to fully understand.

* Binary Tree Inorder Traversal
  - Recursive is trivial
  - [Iterative with stack is easy when I use visited stack](<https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31228/Simple-Python-iterative-solution-by-using-a-visited-flag-O(n)-56ms>)
  - Morris pre/in order is almost the same: the key is to find predecessor, then create thread link, and later delete the link.

## Conclusion

- Implement Queue using Stacks

* Implement Stack using Queues
* Decode String

  - So I haven't fully understand Paranthese evaluation in Basic Calculator I yet!
  - Recursive:
    - when meet open `[`: call recursion to get this `[...]` evaluated and returned a string.
    - when meet closing `]`: break loop.
  - Iterative:
    - use stack

* Flood Fill: please get familiar this classic connected components DFS as in CP3
* Island Perimeter: Perimeter pattern. Use DFS or iteration. The key is process each neighbor.
  - XXX: not familiar with Divide&Conquer recursion (with return value)
* 01 Matrix: not really understand BFS. Reverse thinking: start from 0-node(s)!, then BFS template.
* Keys and Rooms: recursive AC in 1st try. Need to get iterative DFS AC as well!
