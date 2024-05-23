# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prevnode, nextnode = head, None, None
        
        while curr:
            # end of list
            if curr.next is None:
                head = curr
            
            nextnode = curr.next
            curr.next = prevnode
            
            prevnode = curr
            curr = nextnode
            
        return head
            