# Explore Binary Search

- https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/
- Oct 9 - Oct 10, 2021

# Overview

# Intro to BST

- Definition of the BST
  - a special form of binary tree, satisfies the binary search property:
    1. the value in each node must be greater than (or equal to) any values stored in its left subtree
    2. the value in each node must be less than (or equal to) any values stored in its right subtree
  - BST has normal traversal as in general binary tree, but BST's inorder will be in ascending order. So the inorder is most freq used traversal of a BST.

# Basic ops in BST

- Search in BST
  - simple with BST properties
- Insertion in BST
  - Many strategies, here we just use the one which minimizes the changes.
  - search the proper spot, then insert as a leaf.
- Deletion in BST
  - This is more complicated than search/insertion. here we use the one which minimizes the changes: replace the target node with proper child!
  - There're 3 cases.

# Conclusion

- After previous knowledge on BST properties, O(h) search, insert, deletion. We can not use BST for real problems.
- If you want to store data in order and CRUD O(h), use BST.
- Example: Design a class to find the k-th largest element in a stream.
