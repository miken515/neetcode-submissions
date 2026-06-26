# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Solves the Remove Node From End Of Linked List problem.

        Algorithm: Linked List Manipulation
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n) - traverse the linked list
        Space Complexity: O(1) or O(n) - depends on whether new list created
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:  # Iterate until condition fails
            right = right.next
            n -= 1
        
        while right:  # Iterate until condition fails
            left = left.next
            right = right.next
        
        #deleting node
        left.next = left.next.next

        return dummy.next