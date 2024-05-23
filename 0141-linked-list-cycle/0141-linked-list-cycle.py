# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        slow, fast = head, head.next # slow also serves as current
        
        while True:
            if fast is None or fast.next is None:
                return False
            if slow == fast:
                return True
            
            # fast traverses twice as fast
            slow = slow.next
            fast = fast.next.next