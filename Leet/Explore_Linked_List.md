# Explore LInked-List

- 30 items

## Singly Linked List

### Init

1. define Node class with prev/next
2. define `self.head`

## Two Pointers Technique

### Template

- C++ (Neetcode says C++ is A, Python is S, Java is F)
  - Since Python is like pseudo code, easy and short.
  - C++ syntax is short if you familiar with it.
  - Java is cumbersome...

* Code
  ```Python
  slow, fast = head, head
  while slow and fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
          return True
  return False
  ```

### Tips

1. Always examine if the node is null before you call the next field.

   - eg. before we run `fast = fast.next.next`, we need to examine both `fast` and `fast.next` is not null.

2. Carefully define the end conditions of your loop.
   - Run several examples to make sure your end conditions will not result in an endless loop.
   - And you have to take 1st tip into consideration when you define your end conditions.

### Time Complexity

- As Neetcode, use `T` for time complexity, `M` for space complexity (cuz it's memory consumption)

* Linked List problem's `T` is easy.

* Eg. In our previous finding cycle example, let's assume that we move the faster pointer 2 steps each time and move the slower pointer 1 step each time.
  1. if not cycle, then fast takes N/2 times to reach the end.
  2. if has cycle, then fast pointer needs `M times` to catch up the slow, and `M` is the len of cycle.

## Classic Problems

- Reverse Linked List
- Remove Linked List Elements

### Summary - Linked List Classic Problems

1. Going through some test cases will save you time.
2. Feel free to use several pointers at the same time.
3. In many cases, you need to track the previous node of the current node.

## Doubly Linked List

### Init

1. define Node class with prev/next
2. define `self.head, self.tail`

## Conclusion

### Singly vs Doubly

- `delNode(cur)`: `O(N)` for singly, vs `O(1)` for doubly.
  - because `cur` has no prev pointer in singly, so we have to traverse `O(N)` to prev before delete `cur` node.
- `getLast()`: `O(N)` for singly, vs `O(1)` for doubly.
  - cuz we have `self.tail` in doubly.

### static vs dynamic Data struct

- if you need add/delete a node frequently, use linked list.
- if you need to access an element by index often, array might be better choice.
