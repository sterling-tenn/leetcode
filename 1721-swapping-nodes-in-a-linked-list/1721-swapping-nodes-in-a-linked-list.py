# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # Find length of the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Find k-th node from the beginning and the end
        kth_from_start = kth_from_end = head
        for _ in range(k - 1):
            kth_from_start = kth_from_start.next
        
        for _ in range(length - k):
            kth_from_end = kth_from_end.next
        
        # Swap the values
        kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val
        
        return head
