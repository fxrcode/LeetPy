# Explore Recursion II

- https://leetcode.com/explore/learn/card/recursion-ii/
- Oct 3, 2021 -> Oct 5, 2021 ~~Oct 4, 2021~~
- 4 chap, 25 items
- Prerequisites: Stack, Recursion I

## Divide and Conquer

- D&C intro

  - A divide-and-conquer algorithm works by recursively breaking the problem down into two or more subproblems of the same or related type, until these subproblems become simple enough to be solved directly. Then one combines the results of subproblems to form the final solution.
  - D&C differentiate from other recursion by it's divide into 2 OR MORE subproblems. The recursive algs just SINGLE smaller subplem is sometimes called decrease and conquer, eg. Binary Search.

- Classic D&C: Merge Sort

  - Merge Sort is general, stable sort. Also used in external sort.
  - Two way implementations: Top-down or Bottom-up. We explain Top-down since it's natually implemented using recursion.

    ```
    1. In the first step, we divide the list into two sublists.  (Divide)

    2. Then in the next step, we recursively sort the sublists in the previous step.  (Conquer)

    3. Finally we merge the sorted sublists in the above step repeatedly to obtain the final list of sorted elements.  (Combine)
    ```

  - implementation (Top-down)

    ```
    def merge_sort(nums):
        # bottom cases: empty or list of a single element.
        if len(nums) <= 1:
            return nums

        pivot = int(len(nums) / 2)
        left_list = merge_sort(nums[0:pivot])
        right_list = merge_sort(nums[pivot:])
        return merge(left_list, right_list)


    def merge(left_list, right_list):
        left_cursor = right_cursor = 0
        ret = []
        while left_cursor < len(left_list) and right_cursor < len(right_list):
            if left_list[left_cursor] < right_list[right_cursor]:
                ret.append(left_list[left_cursor])
                left_cursor += 1
            else:
                ret.append(right_list[right_cursor])
                right_cursor += 1

        # append what is remained in either of the lists
        ret.extend(left_list[left_cursor:])
        ret.extend(right_list[right_cursor:])

        return ret
    ```

  - implementation (Bottom-up)
    - We normally implement BU iteratively.

- D&C Template

  - Template:

  ```
  1. Divide. Divide the problem S into a set of subproblems: {S1, S2, ..., Sn} where n >= 2. i.e. there're usually more than one subproblem.
  2. Conquer. Solve each subproblem RECURSIVELY.
  3. Combine. Combine the results of each subproblem.
  ```

  - Pseudocode template:

  ```
  def divide_and_conquer(S):
    # (1) divide the problem into a set of subproblems. (n>=2)
    [S1, S2, ..., Sn] = divide(S)

    # (2), Solve the subproblems RECURSIVELY by `divide_and_conquer()`, obtain the results of subproblems as [R1, R2, ..., Rn]
    rets = [divide_and_conquer(Si) for Si in [S1, S2, ..., Sn]]
    [R1, R2, ..., Rn] = rets

    # (3) combine the results of subproblems, and return the COMBINED result of origin problem.
    return combine([R1, R2, ..., Rn])
  ```

  - Practice the divide_and_conquer template with concrete examples
  - Example 1: Validate Binary Search Tree
    - Sometimes, Tree related problems can be solved using divide_and_conquer algorithms.
  - Example 2: Search a 2D Matrix II
    - Given the property of this partial order 2D matrix. We can pick a point as the pivot to divide the matrix into 4 submatrix.
      - Then we can discard one of them based on target vs pivot.
      - We can furthor optimize the search space by wisely pick the pivot point, then we can discard 2 submatrix!

- Classic D&C: Quick Sort

- Master Theorem: analyze D&C

  - Chap 2 of UCB's algs book gave good example: integer multiplication, say both x,y are n bits integer, then divide into higher n/2 bits, and lower n/2 bits. There's 4 recursion call, but Gauss optimized to 3 recursion call.
  - Recurrance relation: `T(n) = a*T(n/b) + f(n)`.

    1. divide the problem "n" into "b" subproblems of equal size, then the size of each subproblem is `n/b`.
    2. call the recursion function "a" times on the subproblems (XXX: I initially thought a === b, but not! Check UCB Chap 2's integer multiply as stated above)
    3. Combine the results from the subproblems.

  - Three cases for Master Theorem:

    ```
    1. a > b^d: T(n) = O(n^loga)
    2. a = b^d: T(n) = O(n^loga * logn)
    3. a < b^d: T(n) = O(n^d)
    ```

  - Example 1: Maximum Depth of Binary Tree

    - divide to 2 subproblems, recursion on both subtrees, then combine. So b = 2, a = 2, d = 0 => case 1: `T(n) = O(n^logb_a) = O(n)`

  - Example 2: Binary Search
    - divide by mid into 2 subarray, only need to recursion on one of subarrays. So b = 2, a = 1 => case 2: `T(n) = O(nlogn)`
  - Example 3: Quick Select
    - It's a bit tricky due to uncertain of pivot. Let's assume always median of input. Then T(n) = T(n/2) + O(n) => a=1, b=2,d=1 => case 3: `T(n) = O(n)`

## Backtracking

- Backtracking is a general algorithm for finding all (or some) solutions to some computational problems (notably Constraint satisfaction problems or CSPs), which incrementally builds candidates to the solution and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot lead to a valid solution.

* Conceptually, one can imagine the procedure of backtracking as the tree traversal.
* Once we can determine if a certain node can't lead to a valid solution, we abandon the current node and backtrack to its parent node to explore other possibilities. It is due to this backtracking behaviour, the backtracking algorithms are often much faster than the brute-force search algorithm, since it eliminates many unnecessary exploration.

- Example 1: A Full Tree of Trie, task: find out if a given word is present in the tree.

  - Brute force search is the traverse all branches.
  - Backtracking check the node and if not possible lead to solution, we back-track: means backtrack to this node's parent, and try this node's other siblings. Aka: pruning.

- Example 2: classical backtrack: N-Queen puzzle.

- Backtracking Template

  ```
  def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return

    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
  ```

  - Example 1: Robot Room Cleaner
  - Example 2: Sudoku Solver

# Recursion to Iterattion

- Unfold Recursion

  - Recursion -> Stack overflow
  - The good news is that we can always convert a recursion to iteration. In order to do so, in general, we use a data structure of stack or queue, which replaces the role of the system call stack during the process of recursion.
  - Eg. Same Tree Check

    - Note: he used deque to do iteration!
    - So it's ok to use stack or deque in Recursion to Iteration transform!

  - To convert a recursion approach to an iteration one, we could perform the following two steps:

    1. We use a stack or queue data structure within the function, to replace the role of the system call stack. At each occurrence of recursion, we simply push the parameters as a new element into the data structure that we created, instead of invoking a recursion.
    2. In addition, we create a loop over the data structure that we created before. The chain invocation of recursion would then be replaced with the iteration within the loop.

# Conclusion

- Beyond Recursion

  - Divde and Conquer VS. Backtracking

    1. D&C has solo solution, while backtracking has unknown number of solutions.

       - eg. merge-sort a list, we obtain a unique sorted list. While there're many solutions to place the queens for the N-Queen problem.

    2. Each step in the D&C problem is `indispensable` to build the final solution, while many steps in Backtracking problem might not lead to solution, but server as `attempts` to search for the potential solution.

       - eg. merge-sort's divide, conquer, combine are all indispensable to build the final sorted list, while there're many trail-and-errors during the process of building solutions for the N-queen problem.

    3. When building the solution in the D&C algs, we have a `clear and predefined` path, though there might be several different manners to build the path. While in the backtracking problems, one does not know in advance the exact path to the solution.
