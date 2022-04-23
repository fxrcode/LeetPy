# Explore Recursion I

- Sept 8, 2021

* 21 items

## Principle of Recursion

- Recursion is an approach to solving problem using a function that calls itself as a subroutine.
  - The trick is that each time a recursive function calls itself, it reduces the given problem into subproblems.
- A recursive function should have 2 properties:
  1. a simple `base case` - terminating scenario that doesn't recurse to produce an answer
  2. A set of rules, also known as `recurrence relation` that reduces all other cases towards the base case.

## Recurrence Relation

- There're 2 important things that one needs to figure out before implementing a recursive function.
  1. recurrence relation: the relationship between the result of a problem and the result of its subproblem.

## Memoization

## Complexity Analysis

### Time Complexity

- time complexity $O(T) = R*O(s)$

  - R: number of recursion invocations
  - O(s) time complexity of calculation incurs along with each recursion call.

- In most cases, it's hard to glance and find # recursion calls. Then we'd better resort to the `execution tree`, which is a tree that is used to denote the execution flow of a recursive function in particular:

  - each node represents an invocation of the recursive function.
  - therefore the # number of nodes in the tree => # of recursion calls during execution.
  - The execution tree of a recursive function would form an `n-ary tree`.
    - `n` as the number of times recursion appears in the recurrence relation.
    - eg. the execution of Fibonaaci function would form a binary tree.
      - In a full binary tree with `n` levels, the total number of nodes = 2^n - 1.
      - Therefore Fibonacci recursive solution is O(2^n)

- Given Memoization, we optimize the recursive solution.
  - eg. Fibonacci/Climb_steps, each Fibonacci calculation occur only once. So time complexity = O(N).
  * memoization not only optimizes the time complexity of algorithm, but also simplifies the calculation of time complexity.

### Space Complexity

- There're 2 parts of space consumption that one should bear in mind when calculating the space complexity of a recursive algorithm:

  1. `recursion related`
  2. `non-recursion related`

- `recursion related space` ![](https://assets.leetcode.com/uploads/2019/01/25/card_recursion_stack.png)
  - Function call stack holds 3 important info:
    1. Returning address of the function call.
    2. The params that passed to the func call.
    3. The local variables within the func call.
- `non-recursion related space`:
  - global variables: eg. input.
  - intermediate result: eg. memo[] hash.

### Tail Recursion

- Tail recursion is a recursion where the recursive call is the `final instruction` in the recursion function. And there should be `only one` recursive call in the function.

* The `benefit of having tail recursion` is that it could avoid the accumulation of stack overheads during the recursive calls, since the system could reuse a fixed amount space in the stack for each recursive call.

* non-tail recursion vs tail recursion:

  ```python
  def sum_non_tail_recursion(ls):
  """
  :type ls: List[int]
  :rtype: int, the sum of the input list.
  """
  if len(ls) == 0:
      return 0

  # not a tail recursion because it does some computation after the recursive call returned.
  return ls[0] + sum_non_tail_recursion(ls[1:])


  def sum_tail_recursion(ls):
      """
      :type ls: List[int]
      :rtype: int, the sum of the input list.
      """
      def helper(ls, acc):
          if len(ls) == 0:
              return acc
          # this is a tail recursion because the final instruction is a recursive call.
          return helper(ls[1:], ls[0] + acc)

      return helper(ls, 0)
  ```

## Conclusion

### Conclusion - Recursion I

- Some tips in solving problems with recursive algorithm
  1. When in doubt, write down the `recurrence relationship`.
  - Sometimes, the relation might not be obvious. It's helpful to deduct some relationships with the help of math formulas, cuz recurrence is close to math.
  - Often, they can clarify the ideas and uncover the hidden `recurrence relation`. eg. `Unique Binary Search Trees II`.
  2. Whenever possible, apply `memoization`.
  3. When stack overflows, `tail recursion` might come to help.
