# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Solves the Reorder Linked List problem.

        Algorithm: Linked List Manipulation
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n) - traverse the linked list
        Space Complexity: O(1) or O(n) - depends on whether new list created
        """
        slow, fast = head, head.next
        while fast and fast.next:  # Iterate until condition fails
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        
        #reversing second part of linked list
        while second:  # Iterate until condition fails
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #merging both
        first, second = head, prev    
        while second:  # Iterate until condition fails
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2