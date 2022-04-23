# Leetcode Explore Trie

- Jan 24, 2022
- https://leetcode.com/explore/learn/card/trie/

## Intro

- Trie, also called prefix tree, is a special form of a Nary tree.
- After completing this card, you should be able to:

  1. Understand the concept of Trie;
  2. Do insertion and search operations in a Trie;
  3. Understand how Trie helps in practical application;
  4. Solve practical problems using Trie.

### What's Trie?

![](../pics/trie-intro.png)

- A Trie is a special form of N-ary tree. Typically, a trie is used to store strings.
- Each trie node represents a string (a prefix).
- Each node might have several children nodes, while the `paths` to different children nodes represent `different chars`.
- The strings the child nodes represent will be the origin str represented by the node itself + `the chars on the path`.

- It's worth noting that the `root` node is associated with the `empty str`
- One important property of Trie is that, all descendants of a node have a common prefix of the string associated with that node. That's why Trie is also called `prefix tree`.

## Basic Operations

### Insertion

- `init a root node` before you insert strings.

### Search

### Implement Trie (Prefix Tree)

- Compare with HashTable
  - We assume there are `N` keys and the maximum length of a key is `M`.
  - Time complexity: HashTable: O(1), Trie: O(M)
  - Space complexity: Trie wins

## Practical Application I

## Practical Application II
