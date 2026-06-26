# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#brute force
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Solves the Merge K Sorted Linked Lists problem.

        Algorithm: Sorting
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n log n) - standard sorting complexity
        Space Complexity: O(1) or O(n) - depends on sorting algorithm
        """
        nodes = []
        for lst in lists:  # Iterate through collection
            while lst:  # Iterate until condition fails
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()

        res = ListNode(0)
        cur = res
        for node in nodes:  # Iterate through collection
            cur.next = ListNode(node)
            cur = cur.next
        return res.next