# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Solves the Add Two Numbers problem.

        Algorithm: Iteration with Carry
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(max(m, n)) - process all elements of both inputs
        Space Complexity: O(max(m, n)) - output length equals max input length
        """
        dummy = ListNode()
        cur = dummy

        carry = 0  # Track carry for addition
        while l1 or l2 or carry:  # Iterate until condition fails
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10  # Track carry for addition
            val = val % 10

            cur.next = ListNode(val)

            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        
        return dummy.next
