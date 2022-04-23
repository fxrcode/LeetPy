# N-ary Tree

- Sep 24, 2021
- 11 items

## Overview

- In previous explore, we focused in Binary Tree. This card extends the concepts you learned in binary tree to N-ary tree.

## Traversal

- pre/post order, because there's no meaning for inorder in N-ary Tree.
- same old technique as Binary Tree traversal: recursion or stack iterative (using visited flag template)
- BFS for inorder

## Recursion

- this section is extend from Binary Tree's `Solve Tree Problems Recursively`
- "Top-down" means that in each recursion level, we will visit the node first to come up with some values, and pass these values to its children when calling the function recursively.

  ```
  1. return specific value for null node
  2. update the answer if needed                              // answer <-- params
  3. for each child node root.children[k]:
  4.      ans[k] = top_down(root.children[k], new_params[k])  // new_params <-- root.val, params
  5. return the answer if needed                              // answer <-- all ans[k]
  ```

- "Bottom-up" means that in each recursion level, we will firstly call the functions recursively for all the children nodes and then come up with the answer according to the return values and the value of the root node itself.
  ```
  1. return specific value for null node
  2. for each child node root.children[k]:
  3.      ans[k] = bottom_up(root.children[k])    // call function recursively for all children
  4. return answer                                // answer <- root.val, all ans[k]
  ```

## Conclusion
