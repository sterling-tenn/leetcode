# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # recursive call
        next_node = self.swapPairs(head.next.next)
        
        # swap pair
        second = head.next
        head.next = next_node
        second.next = head
        head = second
        
        return head
        
        