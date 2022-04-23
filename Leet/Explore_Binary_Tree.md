# Binary Tree

- https://leetcode.com/explore/learn/card/data-structure-tree/
- Sep 23, 2021 - Sep 24, 2021

* 19 items

## Traverse a Tree

- Pre-order Traversal
- In-order Traversal
  - in BST, inorder returned array is also sorted

* Post-order Traversal
  - When you delete nodes in a tree, deletion process will be in post-order.
  - Also, it's widesly used in maths expression.
* Recursive or Iterative

## Solve Problems Recursively

### Top-down

- Top-down: in each recursive call, we'll visit the node first to come up with `some values`, and `pass these values` to its children when calling the function recursively.
  - So the top-down solution is kind of per-order traversal.
- The pseudo code:
  ```python
  1. return specific value for None node
  2. update the answer if needed
  3. left_ans = top_down(root.left, left_params)
  4. right_ans = top_down(root.right, right_params)
  5. return the answer if needed
  ```
- eg. Top-down: find maximum depth of a binary tree
  ```python
  ans = 0
  def max_depth(root: Node, depth: int)->None:
    if not root:
      return
    if not root.left and not root.right:
      nonlocal ans
      ans = max(ans, depth)
    max_depth(root.left, depth+1)
    max_depth(root.right, depth+1)
  ```

### Bottom-up

- Bottom-up: in each recursive call, we will firstly call the function recursively for all the children nodes and then come up with the answer accordingly to the `returned values` and the value of the current node itself.
  - This process can be regarded as a kind of `post-order` traversal.
- Typically, a bottom-up recursive function `bottom_up(root)` will be like:

  ```python
  1. return specific value for the None node
  2. left_ans = bottom_up(root.left)
  3. right_ans = bottom_up(root.right)
  4. return answers
  ```

- Again, we discuss the same maximum depth of binary tree but using a different way of thinking: for a single node of the tree, what will be the maximum depth of the subtree rooted at itself?
  ```python
  return 0 if not root
  left_depth = maximum_depth(root.left)
  right_depth = maximum_depth(root.right)
  return max(left_depth, right_depth)+1
  ```

### Top-down vs Bottom-up

- When you meet a tree problem, ask yourself 2 questions. If both answers yes, try to solve the problem using a top-down recursive solution.

  1. can you determine some params to help the node know its answer?
  2. Can you use these params and the value of the node itself to determine what should be the params passed to its children.

- Or you can think of the problem in this way: for a node in a tree, if you know the answer of its children, can you calcualte the answer of the node? If yes, solveing the problem recursively using a bottom-up approach might be a good idea.

### Questions

- Maximum Depth of Binary Tree
  - example to do top-down vs bottom-up

* Symmetric Tree
  - XXX: Good question on Tree recursion: need helper with 2 nodes so as to compare mirrored subtrees. Thanks for Huahua's 116.Populating Next Right Pointers in Each Node local view analysis.
* Path Sum
  - Top-down appraoch

## Conclusion

- Construct Binary Tree from Inorder and Postorder Traversal
- Construct Binary Tree from Preorder and Inorder Traversal
  - Understand pre/post order's root, then use it to find num_left in inorder.
  - XXX: visualize to do analysis recursion and careful index calculation!
- Populating Next Right Pointers in Each Node
  - XXX: huahua's analysis why pre-order, and local view to study recursion action.
- Populating Next Right Pointers in Each Node II
  - XXX: visualize good example helps to understand why we do modified preorder: process(root), recur(right), recur(left). Because we need `fnext(root.next)`!
- Lowest Common Ancestor of a Binary Tree
  - classic Tree recursion, need to extend the meaning of origin function
- Serialize and Deserialize Binary Tree
  - I did inorder. TODO: preorder.
