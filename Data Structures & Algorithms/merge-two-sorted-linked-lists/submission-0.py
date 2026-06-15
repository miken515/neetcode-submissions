# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = ListNode()
        builder = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tmp = list1.next
                builder.next = list1
                builder = list1
                list1 = tmp
            else:
                tmp = list2.next
                builder.next = list2
                builder = list2
                list2 = tmp
        
        if list1:
            builder.next = list1
        if list2:
            builder.next = list2
        
        return dummy.next