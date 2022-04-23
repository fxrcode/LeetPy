'''
Weekly Contest 271 (Dec 11, 2021)
Only 2/4!
TLE for this problem (Q2)

Similar to leet #907
'''

from typing import List
from heapq import heapify, heappop

# https://leetcode.com/discuss/interview-question/787180/segment-tree-implementation-python-range-query-min-max-sum-and-update-segment-tree


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.min = float("inf")
        self.max = float("-inf")
        self.sum = float("inf")
        self.leftEdge = None
        self.rightEdge = None


class SegmentTree:
    def __init__(self):
        """
        Initializer method to initialize the class level objects
        :rtype: object
        """
        self.partial_overlap = "Partial overlap"
        self.no_overlap = "No overlap"
        self.complete_overlap = "Complete overlap"

    def get_overlap(self, x1, y1, x2, y2):
        """
        Method to get the overlapping type for a given ranges
        X1, Y1 -> Given node's range
        X2, Y2 -> Query range
        :return: type of overlap
        """
        if (x1 == x2 and y1 == y2) or (x1 >= x2 and y1 <= y2):
            overlap = self.complete_overlap
        elif (y1 < x2) or (x1 > y2):
            overlap = self.no_overlap
        else:
            overlap = self.partial_overlap
        return overlap

    def construct_segment_tree(self, array, start, end):
        """
        Method to construct a Segment tree using a given array elements
        :param end:
        :param start:
        :param array: Array elements
        :return: Root node of a segment tree
        """
        if end - start <= 0 or len(array) == 0:
            return None
        if end - start == 1:
            node = Node()
            node.min = array[start]
            node.max = array[start]
            node.sum = array[start]
            node.leftEdge = start
            node.rightEdge = end - 1
            return node
        else:
            node = Node()
            mid = start + (end - start) // 2
            node.left = self.construct_segment_tree(
                array, start=start, end=mid)
            node.right = self.construct_segment_tree(array, start=mid, end=end)
            if node.left is None and node.right is None:
                node.sum = 0
                node.leftEdge = start
                node.rightEdge = start
                node.min = float("inf")
                node.max = float("-inf")
            elif node.left is None:
                node.sum = node.right.sum
                node.leftEdge = node.right.leftEdge
                node.rightEdge = node.right.rightEdge
                node.min = node.right.min
                node.max = node.right.max
            elif node.right is None:
                node.sum = node.left.sum
                node.leftEdge = node.left.leftEdge
                node.rightEdge = node.left.rightEdge
                node.min = node.left.min
                node.max = node.left.max
            else:
                node.min = min(node.left.min, node.right.min)
                node.max = max(node.left.max, node.right.max)
                node.sum = node.left.sum + node.right.sum
                node.leftEdge = node.left.leftEdge
                node.rightEdge = node.right.rightEdge
            return node

    def update_segment_tree(self, head, index, new_value, array):
        """
        Method to update the segment tree node value
        :return: Head node of a segment tree
        :rtype: object
        """
        if index == head.leftEdge == head.rightEdge:
            head.max = new_value
            head.min = new_value
            head.sum = new_value
            array[index] = new_value
            return head
        elif (head.leftEdge <= index <= head.rightEdge) and (head.rightEdge > head.leftEdge):
            left_node = self.update_segment_tree(
                head=head.left, index=index, new_value=new_value, array=array)
            right_node = self.update_segment_tree(
                head=head.right, index=index, new_value=new_value, array=array)
            head.sum = right_node.sum + left_node.sum
            head.min = min(left_node.min, right_node.min)
            head.max = max(left_node.max, right_node.max)
            return head
        else:
            return head

    def get_minimum(self, head, left, right):
        """
        Method to get the minimum in a given range query
        :return: Minimum value for a given range query
        """
        overlap = self.get_overlap(head.leftEdge, head.rightEdge, left, right)
        if overlap == self.complete_overlap:
            return head.min
        elif overlap == self.no_overlap:
            return float("inf")
        elif overlap == self.partial_overlap:
            left_min = self.get_minimum(head=head.left, left=left, right=right)
            right_min = self.get_minimum(
                head=head.right, left=left, right=right)
            return min(left_min, right_min)

    def get_maximum(self, head, left, right):
        """
        Method to get the maximum value for a given range query
        :return Maximum value for a given range query
        """
        overlap = self.get_overlap(head.leftEdge, head.rightEdge, left, right)
        if overlap == self.complete_overlap:
            return head.max
        elif overlap == self.no_overlap:
            return float("-inf")
        elif overlap == self.partial_overlap:
            left_max = self.get_maximum(head=head.left, left=left, right=right)
            right_max = self.get_maximum(
                head=head.right, left=left, right=right)
            return max(left_max, right_max)

    def get_sum(self, head, left, right):
        """
        Method to return the sum of an array elements for a given range query
        :return: Returns the sum of an array elements for a given range query
        """
        overlap = self.get_overlap(head.leftEdge, head.rightEdge, left, right)
        if overlap == self.complete_overlap:
            return head.sum
        elif overlap == self.no_overlap:
            return 0
        elif overlap == self.partial_overlap:
            left_sum = self.get_sum(head=head.left, left=left, right=right)
            right_sum = self.get_sum(head=head.right, left=left, right=right)
            return left_sum + right_sum

    def preorder_traversal(self, head, array):
        if head is None:
            return
        print("Array = {} Min = {}, Max = {}, Sum = {}".format(array[head.leftEdge:head.rightEdge + 1], head.min,
                                                               head.max, head.sum))
        self.preorder_traversal(head=head.left, array=array)
        self.preorder_traversal(head=head.right, array=array)


class Solution:
    def subArrayRanges(self, A: List[int]) -> int:
        def lee215_On2():
            """
            XXX: Smart loop rather loop len, then loop start, which is O(N^3) due to min/max.
            O(N^2)
            """
            res = 0
            n = len(A)
            for i in range(n):
                l = r = A[i]
                for j in range(i, n):
                    l = min(l, A[j])
                    r = max(r, A[j])
                res += r-l
            return res

        def fxr_XYZ123():
            """
            BUG: NEVER randomly Guess math property!
            """
            diff = []
            for i in range(0, len(A), step=2):
                mn, mx = min(A[i], A[i+1]), max(A[i], A[i+1])
                diff.append(mx-mn)
            heapify(diff)
            sm = 0
            while diff:
                sm += sum(diff)
                heappop(sm)
            return sm

        def fxr_segment():
            st = SegmentTree()
            root = st.construct_segment_tree(
                array=A, start=0, end=len(A))
            sm = 0
            for l in range(1, len(A)+1):
                for i in range(0, len(A)-l+1):
                    # ran = nums[i:i+l]
                    # sm += max(ran) - min(ran)
                    start, end = i, i+l-1
                    sm += st.get_maximum(root, start, end) - \
                        st.get_minimum(root, start, end)
            return sm

        def fxr_brute():
            def mnmx(start, end):
                """
                TLE
                """
                mn = 1e10
                mx = -1e10
                for i in range(start, end):
                    n = A[i]
                    mn = min(mn, n)
                    mx = max(mx, n)
                return mx-mn
            sm = 0
            for l in range(1, len(A)+1):
                for i in range(0, len(A)-l+1):
                    # ran = nums[i:i+l]
                    # sm += max(ran) - min(ran)
                    start, end = i, i+l
                    sm += mnmx(start, end)
            return sm
