# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Solves the Reverse A Linked List problem.

        Algorithm: Backtracking
        - Approach: Explore all possibilities with pruning
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(2^n) - exponential search space
        Space Complexity: O(n) - recursion depth and result storage
        """
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None
        return newHead


# Recursive 