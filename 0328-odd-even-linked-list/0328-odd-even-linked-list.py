# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # empty list
        if not head:
            return head
        
        odd = head
        even = head.next
        firstEven = even # so we can reattach the end of odds to it
        
        while even and even.next:
            # skip next node
            odd.next = odd.next.next
            even.next = even.next.next
            
            # traverse
            odd = odd.next
            even = even.next
            
        odd.next = firstEven
        
        return head