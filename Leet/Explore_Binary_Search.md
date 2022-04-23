# Explore Binary Search

- https://leetcode.com/explore/learn/card/binary-search/
- Oct 5 - Oct 6, 2021
- 8 chapters, 30 items

## Overview

- Binary Search is one of the most fundamental and useful algorithm in CS. It describes the process of searching for a specific value in an ordered collection.
- Terminology used:
  - Target: the value that you searching for
  - Index: the current location that you are searching
  - Left/Right: the indices from which we used to maintain our search space
  - Mid: the index that we use to apply a condition on so as to determine if we should search left or right.

* How does it work?

  - we will review how to identify Binary Search problems, reasons why we use Binary Search, and the 3 different Binary Search templates that you might be previously unaware of.

* Identification and Template Introduction

  - Three parts of Successful Binary Search

    1. Pre-process: sort if collections unsorted
    2. Binary Search: Using `iteration` or `RECURSION` to divide search space in half after each comparison.
    3. Post-process: Determine viable candidates in the remaining space.

  - Three Templates for Binary Search
    - When we first learned Binary Search, we might struggle. We might study `hundreds` of Binary Search problems online and each time we looked at a developer's code, it seemed to be `implemented slightly differently`. Although each implementation divided the problem space in 1/2 at each step, one had numerous questions:
    1. Why was it implemented slightly differently?
    2. What was the developer thinking?
    3. Which way was easier?
    4. Which way is better?

# Template I

- Most basic and elementary form of a Binary search.
- Code

  ```python
  def binarySearch(nums, target):
  if len(nums) == 0: return -1

  left, right = 0, len(nums) - 1
  while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
          return mid
      elif nums[mid] < target:
          left = mid + 1
      else:
          right = mid - 1

  # End Condition: left > right
  return -1
  ```

# Template II

- an advanced form of Binary Search. It is used to search for an element or condition which requires accessing the current index and its immediate right neighbor's index in the array.

* Code

  ```python
  def binarySearch(nums, target):
  if len(nums) == 0:
      return -1

  left, right = 0, len(nums)
  while left < right:
      mid = (left + right) // 2
      if nums[mid] == target:
          return mid
      elif nums[mid] < target:
          left = mid + 1
      else:
          right = mid

  # Post-processing:
  # End Condition: left == right
  if left != len(nums) and nums[left] == target:
      return left
  return -1
  ```

# TEmplate III (same as 9chap!!!)

- another unique form of Binary Search. It is used to search for an element or condition which requires accessing the current index and its immediate left and right neighbor's index in the array.

* Code:

  ```python
  def binarySearch(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1
  ```

* Key Attributes:
  - An alternative way to implement Binary Search

# TEmplate Analysis

- Template 1 and 3 are the most commonly used and almost all binary search problems can be easily implemented in one of them.

* Template 2 is a bit more advanced and used for certain types of problems.
* Other Types of Binary Search
  - LC #4: Median of Two Sorted Arrays
