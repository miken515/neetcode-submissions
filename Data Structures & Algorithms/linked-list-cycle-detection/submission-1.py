# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Solves the Linked List Cycle Detection problem.

        Algorithm: Linked List Manipulation
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n) - traverse the linked list
        Space Complexity: O(1) or O(n) - depends on whether new list created
        """
        slow = head
        fast = head

        while fast and fast.next:  # Iterate until condition fails

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False