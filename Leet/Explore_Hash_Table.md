# Hash Table

- Sep 29, 2021 -> ~~Sep 30, 2021~~ Oct 2, 2021
- 35 problems

## Overview

## Design a Hash Table

- The key idea of Hash Table is to use a hash function to map keys to buckets.

* There are two essential factors that you should pay attention to when you are going to design a hash table.
  - Hash Function
  - Collision Resolution
    - Let's assume that the bucket, which holds the maximum number of keys, has N keys.
    - Typically, if N is constant and small, we can simply use an array to store keys in the same bucket.
    - If N is variable or large, we might need to use `height-balanced binary search tree` instead.

## Hash Set

## Hash Map

- Value can be any information you needed (e.g. index)

- Scenario I: Provide more info

  - eg. Given an array of integers, return indices of the two numbers such that they add up to a specific target.

- Scenario II: Aggregate by Key
  - Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
  - The key to solving this kind of problem is to decide your strategy when you encounter an existing key.
    - sum all value? replace with newst one? It depends on the problem.

## Design the Key

- In the previous problems, the choice of key is comparatively straightforward. Unfortunately, sometimes you have to think it over to design a suitable key when using a hash table.

  - eg. Given an array of strings, group anagrams together.
    - ans: our mapping strategy can be: sort the string and use the sorted string as the key. That is to say, both "eat" and "ate" will be mapped to "aet".

- The mapping strategy can be really tricky sometimes.

### Design the Key - Summary

1. When the order of each element in the string/array doesn't matter, you can use sorted string/array as key.
2. If you only care aabout the offset of each value, usally the offset from the 1st value, you can use the offset as the key.
3. In a tree, you might want to directly use the TreeNode as key. But in most cases, serialization of the subtree might be a better idea. (preorder in 652. Find duplicate Subtrees)
4. In a matrix, you may want to use row or col index as key
5. In a Sudoku, you can combine row/col index to identify which box you in: (i,j) -> (i/3)\*3 +j/3
6. Sometimes, in a matrix, you may wan to agreegate the values in the same diagonal line:

- diagonal order: (i,j)->i-j
- anti-diagonal order: (i,j)->i+j

## Conclusion
